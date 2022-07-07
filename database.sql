CREATE TABLE ORDERS (
    order_id INT AUTO_INCREMENT NOT NULL,
    time_in DATETIME NOT NULL,
    time_out DATETIME NOT NULL,
    cost FLOAT NOT NULL,
    pickup INT NOT NULL,
    staff INT NOT NULL,

    PRIMARY KEY (order_id)
    FOREIGN KEY (staff) REFERENCES STAFF (staff_id)
);

CREATE TABLE PRODUCTS (
    product_id INT AUTO_INCREMENT NOT NULL,
    name CHAR(255) NOT NULL,
    price FLOAT NOT NULL,

    PRIMARY KEY (product_id)
);

CREATE TABLE STAFF (
    staff_id INT AUTO_INCREMENT NOT NULL,
    full_name CHAR(255) NOT NULL,
    position CHAR(255) NOT NULL,
    labor_contract INT NOT NULL,

    PRIMARY KEY (staff_id)
);

CREATE TABLE PRODUCTS_ORDERS(
    product_order_id INT AUTO_INCREMENT NOT NULL,
    product INT NOT NULL,
    in_order INT NOT NULL,
    amount INT NOT NULL,

    PRIMARY KEY (product_order_id)
    FOREIGN KEY (product) REFERENCES PRODUCTS (product_id)
    FOREIGN KEY (in_order) REFERENCES ORDERS (order_id)
);


/*********************************************/
/*Сущности для News Portal - NewsPaper project*/
CREATE TABLE USERS(
    user_id INT AUTO_INCREMENT NOT NULL,
    personal_email CHAR(100) NOT NULL,
    pwd CHAR(50) NOT NULL,
    full_name CHAR(255),
    date_reg_u DATETIME NOT NULL,
    date_reg_a DATETIME,
    u_status CHAR(20),

    PRIMARY KEY (user_id)
);


CREATE TABLE ARTICLES(
    article_id INT AUTO_INCREMENT NOT NULL,
    header CHAR(255) NOT NULL,
    short_news CHAR(255) NOT NULL,
    article_text TEXT,
    data_create DATETIME,
    data_release DATETIME,
    a_status CHAR(20),

    PRIMARY KEY (article_id),
);

CREATE TABLE COMMENTS(
    comment_id INT AUTO_INCREMENT NOT NULL,
    comment_text TEXT,
    data_create DATETIME,
    user_comment INT NOT NULL,
    article INT NOT NULL,

    PRIMARY KEY (comment_id),
    FOREIGN KEY (article) REFERENCES ARTICLES (article_id),
    FOREIGN KEY (user_comment) REFERENCES USERS (user_id)
);

CREATE TABLE ARTICLES_USERS(
    article_author_id INT AUTO_INCREMENT NOT NULL,
    author_article INT NOT NULL,
    on_article INT NOT NULL,

    PRIMARY KEY (article_author_id),
    FOREIGN KEY (author_article) REFERENCES USERS (user_id),
    FOREIGN KEY (on_article) REFERENCES ARTICLES (article_id)
);

