import Image from 'next/image'
import Link from 'next/link'
 
export default function Home() {
  return (
    <div className="bg-neutral-950 flex flex-col text-white min-h-screen items-center">
      <h1 className="font-bold text-xl  mt-16">Fin-Manage</h1>
      <h2 className="text-lg mx-12 text-center mt-4">Your personal finance manager</h2>
      <div className="w-screen mt-8 flex flex-row">
        <Image src="/landing-page-1.png" alt="trade market image" width={200} height={200} style={{ borderBottomRightRadius: '20px' }} className="object-cover"/>
        <p className=" text-xs w-[40%] ml-6">
          Take control of your financial journey with our intuitive and powerful personal finance manager app. With Fin-Manage, achieving your financial goals become effortless!
        </p>
      </div>
      <h2 className="text-xl mt-12 mb-6">Key Features</h2>
      <div className="w-screen mt-8 flex flex-row">
        <div className="w-[50%] mr-6">
        <h2 className="text-center mb-2">Track Your Expenses</h2>
        <p className="ml-2 text-xs text-right">
          Reliably track how much you’re spending monthly to have your expenses under control
        </p>
        </div>
        <Image src="/landing-page-2.png" alt="trade market image" width={200} height={200} style={{ borderBottomLeftRadius: '20px' }} className="object-cover"/>
      </div>
      <div className="w-screen mt-8 flex flex-row mb-5">
        <Image src="/landing-page-3.png" alt="saving goals image" width={200} height={200} style={{ borderBottomRightRadius: '20px' }} className="object-cover"/>
        <div className=" w-[50%] ml-6">
          <h2 className="text-center mb-2">Smart Saving Goals</h2>
          <p className=" text-xs mr-2">
            Define your dreams and let Fin-Manage help you achieve them. Set up savings goals, track your progress, and celebrate milestones along the way.
          </p>
        </div>
        
      </div>
      <div className="w-screen mt-8 flex flex-row">
        <div className="w-45 mr-6">
        <h2 className="text-center mb-2">Secutity and Privacy</h2>
        <p className="ml-2 text-xs text-right">
            Your financial data is sensitive, and we take its security seriously. Fin-Manage employs state-of-the-art encryption and security measures to ensure that your information remains confidential and protected.
        </p>
        </div>
        <Image src="/landing-page-4.png" alt="security and privacy image" width={210} height={210} style={{ borderBottomLeftRadius: '20px', }} className="object-cover"/>
      </div>
      <h2 className="text-2xl mt-20">Start Now</h2>
      <Link href="/signup" className="mt-8 bg-cyan-400 p-2 rounded-md w-40 text-center mb-12">Sign Up</Link>
      

    </div>

  )
}
