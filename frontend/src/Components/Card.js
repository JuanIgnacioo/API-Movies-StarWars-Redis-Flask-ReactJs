import React, {useState} from 'react'
import {Redirect} from 'react-router-dom'
import VerCapi from './VerCapi'
import '../bootstrap.min.css'
import $ from 'jquery'


function Card (list){

    const [verCapitulo, estado] = useState('false')



        
        const Style = {
            width : '18rem',
            marginTop: '50px'
        }
    

    if(verCapitulo === 'true'){
        return (<Redirect to={`/ver-capi/${list.list.nombre}`}/>)
        // return (<Redirect to={`/ver-capi/${list.list.nombre}`}/>)       
        
    }

    const verificaEstado =()=>{
    if((list.list.estado === 'reservado')|| (list.list.estado === 'alquilado')){
        return 'btn btn-danger mr-3'
    }else if (list.list.estado === 'disponible'){
        return 'btn btn-info mr-3'
    }else{
        return 'btn btn-info mr-3'
    }
}

       
    return(
    <div  >
            <img src={list.list.foto}  class="card-img-top" style={Style} />
            <div class="card-body">
            <h5 class="card-title mb-2 text-danger ">{list.list.nombre}</h5>
            <button class={verificaEstado()} disabled>{list.list.estado}</button>         
            <button class="btn btn-primary mr-3" onClick={()=> estado('true')} >Ver Capitulo</button>
            
            </div>         
        
        </div>
    )
}
export default Card;

