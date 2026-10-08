# Range-Scalp Bot

*Updated Thu Oct 08 03:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7200 | 6246 | 954 (13) | 0 | $-2184.36 | -4.8% |
| **+10¢** | 5459 | 4337 | 1122 (20) | 0 | $-2119.15 | -6.2% |
| **+15¢** | 4578 | 3394 | 1184 (28) | 0 | $-1759.36 | -6.1% |
| **+20¢** | 4088 | 2858 | 1230 (35) | 0 | $-1389.97 | -5.4% |
| **+10¢ (15¢ stop)** | 8715 | 8693 | 22 (14) | 0 | $-3136.79 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 02:52 | +10 stop | HYPE | DOWN | 0.68 | 0.86 | 1.51 |
| 10-08 02:52 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 10-08 02:52 | +5 | XRP | DOWN | 0.70 | 0.75 | 0.21 |
| 10-08 02:52 | +10 stop | SOL | DOWN | 0.59 | 0.71 | 0.88 |
| 10-08 02:50 | +10 stop | ZEC | UP | 0.71 | 0.52 | -2.23 |
| 10-08 02:50 | +20 | ZEC | UP | 0.71 | no | -7.25 |
| 10-08 02:50 | +15 | ZEC | UP | 0.71 | no | -7.25 |
| 10-08 02:50 | +10 | ZEC | UP | 0.71 | no | -7.25 |
| 10-08 02:50 | +5 | ZEC | UP | 0.71 | no | -7.25 |
| 10-08 02:50 | +10 stop | DOGE | DOWN | 0.54 | 0.74 | 1.68 |
| 10-08 02:50 | +10 stop | BNB | DOWN | 0.57 | 0.76 | 1.59 |
| 10-08 02:50 | +10 stop | ETH | DOWN | 0.61 | 0.75 | 1.09 |
| 10-08 02:50 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 10-08 02:50 | +5 | BNB | DOWN | 0.57 | 0.65 | 0.46 |
| 10-08 02:50 | +10 | HYPE | UP | 0.69 | no | -7.09 |
| 10-08 02:50 | +5 | HYPE | UP | 0.69 | no | -7.09 |
| 10-08 02:50 | +10 stop | SOL | UP | 0.69 | 0.49 | -2.33 |
| 10-08 02:50 | +15 | SOL | UP | 0.69 | no | -7.05 |
| 10-08 02:50 | +10 | SOL | UP | 0.69 | no | -7.05 |
| 10-08 02:50 | +5 | SOL | UP | 0.69 | no | -7.05 |
| 10-08 02:50 | +10 stop | NEAR | UP | 0.65 | 0.48 | -2.04 |
| 10-08 02:50 | +5 | NEAR | UP | 0.65 | no | -6.66 |
| 10-08 02:50 | +5 | XRP | UP | 0.47 | 0.56 | 0.54 |
| 10-08 02:49 | +10 stop | DOGE | UP | 0.62 | 0.43 | -2.25 |
| 10-08 02:49 | +10 stop | BTC | DOWN | 0.53 | 0.68 | 1.16 |
| 10-08 02:48 | +10 stop | HYPE | UP | 0.65 | 0.44 | -2.48 |
| 10-08 02:48 | +20 | HYPE | UP | 0.65 | no | -6.66 |
| 10-08 02:48 | +15 | HYPE | UP | 0.65 | no | -6.66 |
| 10-08 02:48 | +10 | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 10-08 02:48 | +5 | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 10-08 02:48 | +10 stop | SOL | UP | 0.68 | 0.78 | 0.71 |
| 10-08 02:48 | +10 | SOL | UP | 0.68 | 0.78 | 0.71 |
| 10-08 02:48 | +5 | SOL | UP | 0.68 | 0.74 | 0.30 |
| 10-08 02:48 | +10 stop | NEAR | DOWN | 0.54 | 0.38 | -1.95 |
| 10-08 02:48 | +10 stop | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-08 02:47 | +10 stop | BNB | UP | 0.58 | 0.40 | -2.15 |
| 10-08 02:47 | +20 | BNB | UP | 0.58 | no | -5.98 |
| 10-08 02:47 | +15 | BNB | UP | 0.58 | no | -5.98 |
| 10-08 02:47 | +10 | BNB | UP | 0.58 | no | -5.99 |
| 10-08 02:47 | +5 | BNB | UP | 0.59 | 0.65 | 0.29 |
