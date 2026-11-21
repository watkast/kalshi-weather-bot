# Range-Scalp Bot

*Updated Sat Nov 21 15:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 67555 | 58962 | 8593 (134) | 5 | $-18105.16 | -4.3% |
| **+10¢** | 50449 | 40407 | 10042 (175) | 5 | $-16814.38 | -5.3% |
| **+15¢** | 42298 | 31472 | 10826 (225) | 5 | $-15070.19 | -5.7% |
| **+20¢** | 37649 | 26273 | 11376 (283) | 5 | $-13383.74 | -5.7% |
| **+10¢ (15¢ stop)** | 82231 | 82060 | 171 (105) | 0 | $-30184.54 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 15:54 | +10 stop | ZEC | DOWN | 0.68 | 0.80 | 0.92 |
| 11-21 15:52 | +10 stop | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 11-21 15:52 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-21 15:52 | +5 | ETH | DOWN | 0.68 | 0.78 | 0.72 |
| 11-21 15:52 | +10 stop | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-21 15:50 | +10 stop | BNB | DOWN | 0.56 | 0.66 | 0.66 |
| 11-21 15:50 | +10 stop | ZEC | DOWN | 0.58 | 0.71 | 0.97 |
| 11-21 15:50 | +10 stop | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 11-21 15:50 | +10 | NEAR | DOWN | 0.69 | 0.79 | 0.73 |
| 11-21 15:50 | +5 | NEAR | DOWN | 0.69 | 0.74 | 0.21 |
| 11-21 15:49 | +10 stop | DOGE | DOWN | 0.62 | 0.77 | 1.20 |
| 11-21 15:48 | +10 | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-21 15:48 | +10 stop | SOL | DOWN | 0.56 | 0.67 | 0.76 |
| 11-21 15:48 | +10 stop | BTC | DOWN | 0.55 | 0.67 | 0.86 |
| 11-21 15:48 | +10 stop | ETH | DOWN | 0.56 | 0.67 | 0.76 |
| 11-21 15:48 | +20 | ETH | DOWN | 0.56 | 0.78 | 1.89 |
| 11-21 15:48 | +15 | ETH | DOWN | 0.56 | 0.78 | 1.89 |
| 11-21 15:48 | +10 | ETH | DOWN | 0.56 | 0.67 | 0.76 |
| 11-21 15:48 | +5 | ETH | DOWN | 0.56 | 0.63 | 0.35 |
| 11-21 15:47 | +5 | DOGE | DOWN | 0.70 | 0.77 | 0.42 |
| 11-21 15:47 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-21 15:47 | +20 | XRP | DOWN | 0.65 | 0.90 | 2.28 |
| 11-21 15:47 | +15 | XRP | DOWN | 0.65 | 0.81 | 1.33 |
| 11-21 15:47 | +10 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-21 15:47 | +5 | XRP | DOWN | 0.65 | 0.73 | 0.50 |
| 11-21 15:47 | +10 stop | DOGE | DOWN | 0.60 | 0.70 | 0.68 |
| 11-21 15:47 | +20 | DOGE | DOWN | 0.59 | 0.81 | 1.92 |
| 11-21 15:47 | +15 | DOGE | DOWN | 0.60 | 0.77 | 1.40 |
| 11-21 15:47 | +10 | DOGE | DOWN | 0.58 | 0.68 | 0.66 |
| 11-21 15:47 | +5 | DOGE | DOWN | 0.58 | 0.64 | 0.25 |
| 11-21 15:46 | +10 stop | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 11-21 15:46 | +20 | NEAR | DOWN | 0.66 | 0.88 | 1.96 |
| 11-21 15:46 | +15 | NEAR | DOWN | 0.66 | 0.88 | 1.96 |
| 11-21 15:46 | +10 | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 11-21 15:46 | +5 | NEAR | DOWN | 0.66 | 0.75 | 0.60 |
| 11-21 15:46 | +10 stop | HYPE | UP | 0.66 | 0.51 | -1.84 |
| 11-21 15:46 | +20 | HYPE | UP | 0.66 | open |  |
| 11-21 15:46 | +15 | HYPE | UP | 0.66 | open |  |
| 11-21 15:46 | +10 | HYPE | UP | 0.66 | open |  |
| 11-21 15:46 | +5 | HYPE | UP | 0.66 | open |  |
