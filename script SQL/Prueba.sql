

CREATE TABLE Colonia(

    CvColonia        INT             AUTO_INCREMENT,

    NombreColonia    VARCHAR(150),

    CodigoPostal     VARCHAR(10),

    CvMunicipio      INT             NOT NULL,

    PRIMARY KEY (CvColonia)

)ENGINE=MYISAM

;







-- 

-- TABLE: Direccion 

--



CREATE TABLE Direccion(

    CvDireccion    INT             AUTO_INCREMENT,

    Calle          VARCHAR(200),

    NumInt         CHAR(10),

    NumExt         CHAR(10),

    CvColonia      INT             NOT NULL,

    PRIMARY KEY (CvDireccion)

)ENGINE=MYISAM

;







-- 

-- TABLE: Estado 

--



CREATE TABLE Estado(

    CvEstado        INT            AUTO_INCREMENT,

    NombreEstado    VARCHAR(60),

    CvPais          INT            NOT NULL,

    PRIMARY KEY (CvEstado)

)ENGINE=MYISAM

;







-- 

-- TABLE: Municipio 

--



CREATE TABLE Municipio(

    CvMunicipio        INT             AUTO_INCREMENT,

    NombreMunicipio    VARCHAR(100),

    CvEstado           INT             NOT NULL,

    PRIMARY KEY (CvMunicipio)

)ENGINE=MYISAM

;







-- 

-- TABLE: Colonia 

--



ALTER TABLE Colonia ADD CONSTRAINT RefMunicipio2 

    FOREIGN KEY (CvMunicipio)

    REFERENCES Municipio(CvMunicipio)

;





-- 

-- TABLE: Direccion 

--



ALTER TABLE Direccion ADD CONSTRAINT RefColonia1 

    FOREIGN KEY (CvColonia)

    REFERENCES Colonia(CvColonia)

;





-- 

-- TABLE: Municipio 

--



ALTER TABLE Municipio ADD CONSTRAINT RefEstado3 

    FOREIGN KEY (CvEstado)

    REFERENCES Estado(CvEstado)

;





