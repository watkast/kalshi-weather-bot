# Range-Scalp Bot

*Updated Wed Nov 04 21:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47578 | 41424 | 6154 (73) | 3 | $-13752.43 | -4.6% |
| **+10¢** | 35548 | 28411 | 7137 (98) | 4 | $-12567.69 | -5.6% |
| **+15¢** | 29781 | 22096 | 7685 (126) | 4 | $-11513.22 | -6.2% |
| **+20¢** | 26462 | 18412 | 8050 (166) | 4 | $-10173.43 | -6.1% |
| **+10¢ (15¢ stop)** | 57999 | 57906 | 93 (56) | 3 | $-21603.39 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 21:52 | +10 stop | ZEC | DOWN | 0.64 | open |  |
| 11-04 21:52 | +15 | ZEC | DOWN | 0.64 | open |  |
| 11-04 21:52 | +10 | ZEC | DOWN | 0.64 | open |  |
| 11-04 21:52 | +5 | ZEC | DOWN | 0.64 | open |  |
| 11-04 21:52 | +10 stop | DOGE | DOWN | 0.58 | open |  |
| 11-04 21:52 | +20 | DOGE | DOWN | 0.58 | open |  |
| 11-04 21:52 | +15 | DOGE | DOWN | 0.58 | open |  |
| 11-04 21:52 | +10 | DOGE | DOWN | 0.58 | open |  |
| 11-04 21:52 | +5 | DOGE | DOWN | 0.58 | 0.67 | 0.56 |
| 11-04 21:52 | +10 stop | XRP | DOWN | 0.61 | open |  |
| 11-04 21:49 | +10 stop | ETH | UP | 0.46 | 0.27 | -2.22 |
| 11-04 21:49 | +10 stop | XRP | UP | 0.61 | 0.33 | -3.13 |
| 11-04 21:49 | +15 | XRP | UP | 0.61 | open |  |
| 11-04 21:49 | +10 | XRP | UP | 0.61 | open |  |
| 11-04 21:49 | +5 | XRP | UP | 0.61 | open |  |
| 11-04 21:49 | +10 stop | DOGE | UP | 0.58 | 0.43 | -1.86 |
| 11-04 21:49 | +10 stop | NEAR | DOWN | 0.63 | 0.74 | 0.79 |
| 11-04 21:48 | +5 | HYPE | UP | 0.52 | open |  |
| 11-04 21:47 | +10 stop | HYPE | UP | 0.53 | 0.36 | -2.05 |
| 11-04 21:47 | +20 | HYPE | UP | 0.53 | open |  |
| 11-04 21:47 | +15 | HYPE | UP | 0.53 | open |  |
| 11-04 21:47 | +10 | HYPE | UP | 0.53 | open |  |
| 11-04 21:47 | +5 | HYPE | UP | 0.53 | 0.59 | 0.25 |
| 11-04 21:47 | +10 stop | DOGE | UP | 0.51 | 0.63 | 0.85 |
| 11-04 21:47 | +10 stop | SOL | DOWN | 0.53 | 0.75 | 1.88 |
| 11-04 21:47 | +10 stop | ETH | DOWN | 0.54 | 0.39 | -1.85 |
| 11-04 21:47 | +20 | ETH | DOWN | 0.54 | 0.79 | 2.20 |
| 11-04 21:47 | +15 | ETH | DOWN | 0.54 | 0.72 | 1.47 |
| 11-04 21:47 | +10 | ETH | DOWN | 0.54 | 0.72 | 1.47 |
| 11-04 21:47 | +5 | ETH | DOWN | 0.54 | 0.72 | 1.47 |
| 11-04 21:46 | +10 stop | XRP | UP | 0.55 | 0.70 | 1.17 |
| 11-04 21:46 | +20 | XRP | UP | 0.55 | open |  |
| 11-04 21:46 | +15 | XRP | UP | 0.55 | 0.70 | 1.17 |
| 11-04 21:46 | +10 | XRP | UP | 0.55 | 0.70 | 1.17 |
| 11-04 21:46 | +5 | XRP | UP | 0.55 | 0.70 | 1.17 |
| 11-04 21:46 | +10 stop | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-04 21:46 | +20 | BTC | DOWN | 0.57 | 0.79 | 1.90 |
| 11-04 21:46 | +15 | BTC | DOWN | 0.57 | 0.76 | 1.59 |
| 11-04 21:46 | +10 | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-04 21:46 | +5 | BTC | DOWN | 0.57 | 0.67 | 0.66 |
