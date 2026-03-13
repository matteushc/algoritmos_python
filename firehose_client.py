import json
import logging
import boto3
import backoff
from botocore.exceptions import ClientError

import time
from typing import List
from concurrent import futures


logger = logging.getLogger(__name__)

class FirehoseClient:
    """
    AWS Firehose client to send records and monitor metrics.

    Attributes:
        config (object): Configuration object with delivery stream name and region.
        delivery_stream_name (str): Name of the Firehose delivery stream.
        region (str): AWS region for Firehose and CloudWatch clients.
        firehose (boto3.client): Boto3 Firehose client.
        cloudwatch (boto3.client): Boto3 CloudWatch client.
    """

    def __init__(self, config):
        """
        Initialize the FirehoseClient.

        Args:
            config (object): Configuration object with delivery stream name and region.
        """
        self.config = config
        self.delivery_stream_name = config.delivery_stream_name
        self.region = config.region
        self.firehose = boto3.client("firehose", region_name=self.region)
        self.cloudwatch = boto3.client("cloudwatch", region_name=self.region)


    @backoff.on_exception(
        backoff.expo, (ClientError, Exception), max_tries=5, jitter=backoff.full_jitter
    )
    def put_record_batch(self, data: list, batch_size: int = 500):
        """
        Put records in batches to Firehose with backoff and retry.

        Args:
            data (list): List of data records to be sent to Firehose.
            batch_size (int): Number of records to send in each batch. Default is 500.

        This method attempts to send records in batches to the Firehose delivery stream.
        It retries with exponential backoff in case of exceptions.
        """
        for i in range(0, len(data), batch_size):
            batch = data[i : i + batch_size]
            record_dicts = [{"Data": json.dumps(record)} for record in batch]
            try:
                response = self.firehose.put_record_batch(
                    DeliveryStreamName=self.delivery_stream_name, Records=record_dicts
                )
                self._log_batch_response(response, len(batch))
            except Exception as e:
                logger.info(f"Failed to send batch of {len(batch)} records. Error: {e}")


    def send_batch_firehose (self, batch):
        response = self.firehose_client.put_record_batch(
            DeliveryStreamName=self.config.firehose_stream,
            Records=batch
        )
        failed_count = response.get('Failed PutCount', 0)
        error_list = []
    
        if failed_count > 0:
    
            for i, result in enumerate(response[ 'RequestResponses']):
                if 'ErrorCode' in result:
                    error_list.append(batch[i])
        return error_list


    def send_batch(self, records: List[dict]) -> List[dict]:
        try:
    
            chunks = []
            for i in range(0, len(records), 500):
                batch = records[i: i + 500]
                chunks.append(batch)
            with futures.ThreadPoolExecutor (max_workers=10) as executor:
                futures_list = [executor.submit (self.send_batch_firehose, chunk) for chunk in chunks]
                all_errors = []
                for future in futures.as_completed (futures_list):
                    lista_erros = future.result()
                    all_errors.extend(lista_erros)
            time.sleep(2)
            if all_errors:
                self.send_batch(all_errors)
        
        except Exception as e:
            logger.error(
                {
                    "metodo":"send batch",
                    "sg": f"Erro ao enviar dados para o mesh: {str(e)}"
                }
            )

