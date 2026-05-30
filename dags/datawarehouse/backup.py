def backup():
    
    with DAG(
    dag_id = 'produce_json',
    default_args=default_args,
    description='DAG to produce JSON file with raw data',
    schedule ='0 14 * * *',
    catchup=False
) as dag:
    
    # Define tasks
    playlist_id = get_playlist_id()
    video_ids = get_video_ids(playlist_id)
    extract_data = extract_video_data(video_ids)
    save_to_json_task = save_to_json(extract_data)
    
    # Define dependencies
    playlist_id >> video_ids >> extract_data >> save_to_json_task