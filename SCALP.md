# Range-Scalp Bot

*Updated Thu Nov 12 19:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57167 | 49840 | 7327 (101) | 4 | $-15693.07 | -4.4% |
| **+10¢** | 42732 | 34180 | 8552 (133) | 4 | $-14637.41 | -5.4% |
| **+15¢** | 35825 | 26619 | 9206 (167) | 4 | $-13241.78 | -5.9% |
| **+20¢** | 31918 | 22259 | 9659 (217) | 4 | $-11606.19 | -5.8% |
| **+10¢ (15¢ stop)** | 69719 | 69591 | 128 (78) | 0 | $-25723.31 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 19:27 | +10 stop | ETH | DOWN | 0.36 | 0.57 | 1.75 |
| 11-12 19:27 | +5 | ETH | DOWN | 0.36 | 0.57 | 1.75 |
| 11-12 19:27 | +10 stop | HYPE | DOWN | 0.61 | 0.38 | -2.60 |
| 11-12 19:27 | +10 | HYPE | DOWN | 0.63 | open |  |
| 11-12 19:27 | +5 | HYPE | DOWN | 0.62 | open |  |
| 11-12 19:26 | +10 stop | ETH | UP | 0.44 | 0.55 | 0.74 |
| 11-12 19:26 | +20 | ETH | UP | 0.44 | 0.64 | 1.65 |
| 11-12 19:26 | +15 | ETH | UP | 0.47 | 0.64 | 1.35 |
| 11-12 19:26 | +10 | ETH | UP | 0.47 | 0.64 | 1.35 |
| 11-12 19:26 | +5 | ETH | UP | 0.47 | 0.55 | 0.44 |
| 11-12 19:26 | +10 stop | ZEC | DOWN | 0.57 | 0.69 | 0.87 |
| 11-12 19:25 | +10 stop | HYPE | UP | 0.58 | 0.38 | -2.35 |
| 11-12 19:24 | +10 stop | XRP | DOWN | 0.71 | 0.81 | 0.74 |
| 11-12 19:24 | +10 stop | ZEC | DOWN | 0.56 | 0.38 | -2.15 |
| 11-12 19:24 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.50 |
| 11-12 19:23 | +10 stop | DOGE | DOWN | 0.55 | 0.69 | 1.07 |
| 11-12 19:23 | +20 | DOGE | DOWN | 0.55 | 0.81 | 2.31 |
| 11-12 19:23 | +15 | DOGE | DOWN | 0.55 | 0.74 | 1.58 |
| 11-12 19:23 | +10 | DOGE | DOWN | 0.55 | 0.69 | 1.07 |
| 11-12 19:23 | +5 | DOGE | DOWN | 0.55 | 0.60 | 0.15 |
| 11-12 19:23 | +10 stop | BTC | DOWN | 0.64 | 0.80 | 1.31 |
| 11-12 19:23 | +10 stop | HYPE | UP | 0.57 | 0.67 | 0.66 |
| 11-12 19:22 | +10 stop | XRP | DOWN | 0.70 | 0.54 | -1.93 |
| 11-12 19:22 | +10 stop | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-12 19:22 | +10 stop | ZEC | UP | 0.63 | 0.48 | -1.85 |
| 11-12 19:22 | +20 | ZEC | UP | 0.63 | open |  |
| 11-12 19:22 | +15 | ZEC | UP | 0.63 | open |  |
| 11-12 19:22 | +10 | ZEC | UP | 0.63 | open |  |
| 11-12 19:22 | +5 | ZEC | UP | 0.63 | open |  |
| 11-12 19:22 | +5 | BTC | UP | 0.60 | open |  |
| 11-12 19:20 | +5 | NEAR | UP | 0.60 | open |  |
| 11-12 19:19 | +10 stop | NEAR | UP | 0.52 | 0.30 | -2.57 |
| 11-12 19:19 | +20 | NEAR | UP | 0.52 | open |  |
| 11-12 19:19 | +15 | NEAR | UP | 0.52 | open |  |
| 11-12 19:19 | +10 | NEAR | UP | 0.52 | open |  |
| 11-12 19:19 | +5 | NEAR | UP | 0.52 | 0.59 | 0.35 |
| 11-12 19:19 | +15 | BTC | UP | 0.59 | open |  |
| 11-12 19:19 | +10 stop | XRP | UP | 0.58 | 0.42 | -1.96 |
| 11-12 19:19 | +20 | XRP | UP | 0.58 | 0.91 | 3.05 |
| 11-12 19:19 | +15 | XRP | UP | 0.58 | 0.91 | 3.05 |
