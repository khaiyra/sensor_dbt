CREATE TABLE IF NOT EXISTS 'StationSummary'
(
    'ID' INT NOT NULL AUTO_INCREMENT, 
    'flow_99' FLOAT DEFAULT NULL,
    'flow_max' FLOAT DEFAULT NULL,
    'flow_median' FLOAT DEFAULT NULL,
    'flow_total' FLOAT DEFAULT NULL,
    'n_obs' INT DEFAULT NULL,
    PRIMARY KEY ('ID')
);