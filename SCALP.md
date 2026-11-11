# Range-Scalp Bot

*Updated Wed Nov 11 11:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55737 | 48606 | 7131 (94) | 2 | $-15238.39 | -4.3% |
| **+10¢** | 41650 | 33332 | 8318 (124) | 3 | $-14180.13 | -5.4% |
| **+15¢** | 34918 | 25945 | 8973 (158) | 4 | $-12960.61 | -5.9% |
| **+20¢** | 31098 | 21686 | 9412 (208) | 5 | $-11329.59 | -5.8% |
| **+10¢ (15¢ stop)** | 67902 | 67781 | 121 (73) | 1 | $-24990.21 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 11:24 | +10 stop | ZEC | DOWN | 0.61 | open |  |
| 11-11 11:23 | +10 stop | SOL | DOWN | 0.52 | 0.32 | -2.29 |
| 11-11 11:22 | +10 stop | BTC | UP | 0.63 | 0.47 | -1.95 |
| 11-11 11:22 | +10 stop | ETH | DOWN | 0.54 | 0.68 | 1.06 |
| 11-11 11:22 | +10 stop | DOGE | DOWN | 0.53 | 0.70 | 1.37 |
| 11-11 11:22 | +10 stop | NEAR | DOWN | 0.54 | 0.73 | 1.58 |
| 11-11 11:22 | +10 stop | ZEC | UP | 0.54 | 0.31 | -2.63 |
| 11-11 11:21 | +10 stop | SOL | UP | 0.59 | 0.42 | -2.05 |
| 11-11 11:21 | +5 | SOL | UP | 0.59 | 0.66 | 0.37 |
| 11-11 11:21 | +10 stop | ETH | UP | 0.63 | 0.42 | -2.45 |
| 11-11 11:21 | +10 stop | NEAR | UP | 0.67 | 0.42 | -2.84 |
| 11-11 11:21 | +10 stop | DOGE | UP | 0.60 | 0.42 | -2.15 |
| 11-11 11:20 | +15 | SOL | DOWN | 0.49 | open |  |
| 11-11 11:20 | +5 | SOL | DOWN | 0.49 | 0.55 | 0.24 |
| 11-11 11:20 | +10 stop | XRP | DOWN | 0.48 | 0.66 | 1.46 |
| 11-11 11:20 | +10 | XRP | DOWN | 0.48 | 0.66 | 1.46 |
| 11-11 11:20 | +5 | XRP | DOWN | 0.48 | 0.66 | 1.46 |
| 11-11 11:20 | +10 stop | HYPE | DOWN | 0.66 | 0.80 | 1.12 |
| 11-11 11:20 | +10 | HYPE | DOWN | 0.66 | 0.80 | 1.12 |
| 11-11 11:20 | +5 | HYPE | DOWN | 0.66 | 0.80 | 1.12 |
| 11-11 11:20 | +10 stop | BTC | UP | 0.59 | 0.69 | 0.68 |
| 11-11 11:20 | +10 stop | NEAR | DOWN | 0.57 | 0.40 | -2.05 |
| 11-11 11:20 | +20 | NEAR | DOWN | 0.57 | open |  |
| 11-11 11:20 | +15 | NEAR | DOWN | 0.57 | 0.73 | 1.28 |
| 11-11 11:20 | +10 | NEAR | DOWN | 0.57 | 0.73 | 1.28 |
| 11-11 11:20 | +5 | NEAR | DOWN | 0.57 | 0.73 | 1.28 |
| 11-11 11:20 | +10 stop | BNB | DOWN | 0.65 | 0.48 | -2.04 |
| 11-11 11:20 | +10 | BNB | DOWN | 0.65 | 0.76 | 0.81 |
| 11-11 11:20 | +5 | BNB | DOWN | 0.65 | 0.71 | 0.29 |
| 11-11 11:19 | +10 stop | ETH | DOWN | 0.65 | 0.36 | -3.23 |
| 11-11 11:19 | +10 stop | DOGE | DOWN | 0.68 | 0.51 | -2.04 |
| 11-11 11:18 | +10 stop | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-11 11:18 | +20 | XRP | DOWN | 0.65 | 0.87 | 1.96 |
| 11-11 11:18 | +15 | XRP | DOWN | 0.65 | 0.87 | 1.96 |
| 11-11 11:18 | +10 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
| 11-11 11:18 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
| 11-11 11:18 | +10 stop | SOL | DOWN | 0.64 | 0.48 | -1.97 |
| 11-11 11:18 | +10 | SOL | DOWN | 0.64 | open |  |
| 11-11 11:18 | +5 | SOL | DOWN | 0.64 | 0.72 | 0.46 |
| 11-11 11:18 | +10 stop | ZEC | DOWN | 0.64 | 0.48 | -1.96 |
