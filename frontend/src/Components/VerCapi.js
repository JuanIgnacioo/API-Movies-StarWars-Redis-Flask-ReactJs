import React, { useState, useEffect, Fragment} from 'react'
import {Redirect,Link} from 'react-router-dom'
import axios from 'axios'
import Swal from 'sweetalert2'
import vader from '../Images/unnamed.png'
import fondo from '../Images/estrellamuerte.jpg'

function VerCapi (codigo){

    const [estado, setEstado] = useState('')
    const [precio, setPrecio] = useState('')
    const [nombre, setNombre] = useState('')
    const [descripcion, setDescripcion] = useState('')
    const [foto, setFoto] = useState('')

    const[pagar,setPagar] = useState('false')
    const [reservar, setReservar] = useState('false')

    const[redirigir,setRedirigir] = useState('false')

    
 
   

//Peticion para traer el listado actualizado
    const actualizarListado = () => {
          axios.get('http://localhost:5000/obtenerListado').then((res) => {
          console.log(res.data)
          console.log(codigo.codigo)
          let capbuscado = res.data.filter(cap => cap.nombre === codigo.codigo)
          
          setNombre(capbuscado[0].nombre)
          setPrecio(capbuscado[0].precio)
          setDescripcion(capbuscado[0].descripcion) 
          setFoto(capbuscado[0].foto) 
          setEstado(capbuscado[0].estado)   
  
        })
        .catch((error) =>{
            console.log(error);
        })        
        
    }

       

    const pagarChapter =(nombre)=> {
      // setPagar('true')
      // if (pagar === 'true'){

      if(estado === 'reservado'){
        
        axios({
          "method" : "POST",
          "url": "http://localhost:5000/pagarCapitulo",
          "params": {
              "capitulo": nombre.nombre,
          }
        }
        ).then((res)=>{
          if(res.data === 'Pagado'){
            Swal.fire({
              title: 'Episodio Alquilado!',
              text: 'Usted alquilo' + nombre.nombre,
              imageUrl: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQe8Z-Gto0cSV7IZ3YWy252MdoooBvv0I-kmBOhoUQaSDADwwk2&usqp=CAU',
              imageWidth: 400,
              imageHeight: 200,
              imageAlt: 'Custom image',
            }).then((result) =>{
              if (result.value){
                let link = '/'
                window.location.href = link
              }
            })
            
            
          }else if (res.data == 'falta reservarlo o se encuentra alquilado'){
            Swal.fire({
              title: 'No se pudo alquilar!',
              text: '(Quizas ya se alquilo o debes reservarlo)',
              imageUrl: 'https://static3.srcdn.com/wordpress/wp-content/uploads/2017/05/Star-Wars-Revenge-of-the-Sith-adaptation-Dark-Horse.jpg',          
              imageWidth: 400,
              imageHeight: 200,
              imageAlt: 'Custom image',
            })
          }
        }).catch((error) =>{
          console.log(error);
        })
      }else {
        console.log('entroxelse')
        Swal.fire({
          title: 'No se pudo alquilar!',
          text: '(Quizas ya se alquilo o debas reservarlo)',
          imageUrl: 'https://static3.srcdn.com/wordpress/wp-content/uploads/2017/05/Star-Wars-Revenge-of-the-Sith-adaptation-Dark-Horse.jpg',          
          imageWidth: 400,
          imageHeight: 200,
          imageAlt: 'Custom image',
        })
      }
      // }
    
    }

    

//PETICION PARA RESERVAR UN CAPITULO
    const reservarCapitulo =(nombre)=> {
     
      if(estado ==='disponible'){
      
        console.log(nombre.nombre)
        axios({
          "method" : "POST",
          "url": "http://localhost:5000/reservarCapitulo",
          "params": {
              "capitulo": nombre.nombre,
          }
        }
        ).then((res)=>{
          if(res.data === 'Reservado con exito'){
            Swal.fire({
              title: 'Episodio Reservado!',
              text: 'Usted reservo el episodio',
              imageUrl: 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQe8Z-Gto0cSV7IZ3YWy252MdoooBvv0I-kmBOhoUQaSDADwwk2&usqp=CAU',
              imageWidth: 400,
              imageHeight: 200,
              imageAlt: 'Custom image',
            }).then((result) =>{
              if (result.value){
                let link = '/'
                window.location.href = link
              }
            })
            
            
            
          }else if (res.data == 'Ya se encuentra reservado o alquilado'){
            Swal.fire({
              title: 'No se pudo reservar!',
              text: '(Quizas ya se alquilo o esta reservado)',
              imageUrl: 'https://static3.srcdn.com/wordpress/wp-content/uploads/2017/05/Star-Wars-Revenge-of-the-Sith-adaptation-Dark-Horse.jpg',          
              imageWidth: 400,
              imageHeight: 200,
              imageAlt: 'Custom image',
            })
          }
        }).catch((error) =>{
          console.log(error);
        })
      

    }else{
      console.log(estado)
      Swal.fire({
        title: 'No se pudo reservar!',
        text: '(Quizas ya se alquilo o esta reservado)',
        imageUrl: 'https://static3.srcdn.com/wordpress/wp-content/uploads/2017/05/Star-Wars-Revenge-of-the-Sith-adaptation-Dark-Horse.jpg',          
        imageWidth: 400,
        imageHeight: 200,
        imageAlt: 'Custom image',
      })
    }
   }

   

    const Style ={
        
        float : 'left',
        // paddingLeft: '10px',
        paddingTop: '10px',
        // marginLeft: '57px',
        position : 'relative',
        widht: '45%',
        height: 'auto',
        // marginRight: 'auto',
      // marginLeft: 'auto'
    }

    const vaderStyle={
      marginTop : '10px',
      float: 'right',
      paddingTop: '10px',
      width: '45%',
      height: 'auto',
      paddingleft: '10px',
      position: 'relative',
      marginRight: 'auto',
      marginLeft: 'auto'
      
    
    }

    const content={
      widht: '100%'
    }

    const container ={
      
      
    }

    const body ={
      backgroundImage: `url(${fondo})`,
      backgroundPosition: 'center',
      height: '100vh',
      overflowY:'hidden',
      overflowX:'hidden'
    }
    

    const t ={
      widht: '100%',
      
    }
    
    useEffect(() => {
      
        actualizarListado();
       
        ;
        
        
    }, [])

    return (
     
       <body style={body}>
      <div className="container col-xl-12 ml-0 mr-0" >
              <div class=" content col-xl-6" style={vaderStyle} >
                        <div class="right" >
                      
                          <img class ="img-fluid animated fadeInRight " align="right" src={vader}></img>
                          <div align="center">
                          <ul>
                            
                          <h4 class="animated fadeInRight text-danger"> Precio : ${precio} </h4>
                          <button type="button" class="btn btn-info btn-sm mr-3 animated fadeInRight delay-1s " onClick={()=> pagarChapter({nombre})}>Alquilar</button>
                          <button type="button" class="btn btn-info btn-sm mr-2 animated fadeInRight delay-1s" onClick={()=> reservarCapitulo({nombre})} >Reservar</button> 
                          <Link to="/" type="button" class="btn btn-info btn-sm mr-2 animated fadeInRight delay-1s">Home</Link>                       
                          </ul>
                          </div>
                          </div>                         
                        
              </div>


        <div className="content col-xl-6 mr-5 pr-5 mb-3" style={Style}>
            <div class="left" >  
                
                  <div >                    
                    <img class="img-fluid animated fadeInLeft" align="left" src={foto} alt="" width="400" height="500"/>
                  </div>   

            </div>   

      </div>

      <div class ="col-sm-6 text-center ml-0 animated fadeInLeft" style={t} >
                    <h3 className="mb-3 text-danger" align="left" >{nombre}</h3>                    
                    <figcaption className="text-justify text-xs-left text-danger">{descripcion}</figcaption>  
                 </div>

     
    </div>
    </body>
)
    }
export default VerCapi;