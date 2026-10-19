# Range-Scalp Bot

*Updated Mon Oct 19 02:58 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23363 | 20313 | 3050 (30) | 1 | $-6978.37 | -4.7% |
| **+10¢** | 17580 | 14065 | 3515 (44) | 1 | $-6213.19 | -5.6% |
| **+15¢** | 14736 | 10946 | 3790 (66) | 1 | $-5656.85 | -6.1% |
| **+20¢** | 13047 | 9083 | 3964 (84) | 1 | $-5022.48 | -6.1% |
| **+10¢ (15¢ stop)** | 28766 | 28715 | 51 (30) | 0 | $-10924.87 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 02:57 | +10 stop | ETH | DOWN | 0.55 | 0.26 | -3.22 |
| 10-19 02:57 | +20 | ETH | DOWN | 0.55 | open |  |
| 10-19 02:57 | +15 | ETH | DOWN | 0.54 | open |  |
| 10-19 02:57 | +10 | ETH | DOWN | 0.54 | open |  |
| 10-19 02:57 | +5 | ETH | DOWN | 0.54 | open |  |
| 10-19 02:55 | +10 stop | NEAR | UP | 0.66 | 0.30 | -3.91 |
| 10-19 02:51 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-19 02:51 | +10 stop | NEAR | UP | 0.60 | 0.77 | 1.40 |
| 10-19 02:50 | +10 stop | ZEC | UP | 0.58 | 0.38 | -2.35 |
| 10-19 02:48 | +10 stop | BNB | UP | 0.69 | 0.85 | 1.36 |
| 10-19 02:47 | +10 stop | ETH | UP | 0.58 | 0.81 | 2.01 |
| 10-19 02:47 | +10 | ETH | UP | 0.57 | 0.67 | 0.66 |
| 10-19 02:47 | +10 stop | NEAR | UP | 0.60 | 0.87 | 2.45 |
| 10-19 02:47 | +10 stop | DOGE | UP | 0.53 | 0.70 | 1.37 |
| 10-19 02:47 | +20 | DOGE | UP | 0.53 | 0.91 | 3.57 |
| 10-19 02:47 | +15 | DOGE | UP | 0.53 | 0.70 | 1.37 |
| 10-19 02:47 | +10 | DOGE | UP | 0.53 | 0.70 | 1.37 |
| 10-19 02:47 | +5 | DOGE | UP | 0.53 | 0.70 | 1.37 |
| 10-19 02:47 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 10-19 02:47 | +5 | ETH | UP | 0.57 | 0.63 | 0.25 |
| 10-19 02:47 | +10 stop | XRP | UP | 0.69 | 0.83 | 1.15 |
| 10-19 02:47 | +20 | XRP | UP | 0.69 | 0.93 | 2.21 |
| 10-19 02:47 | +15 | XRP | UP | 0.69 | 0.87 | 1.57 |
| 10-19 02:47 | +10 | XRP | UP | 0.69 | 0.83 | 1.15 |
| 10-19 02:47 | +5 | XRP | UP | 0.69 | 0.83 | 1.15 |
| 10-19 02:46 | +10 stop | ETH | UP | 0.48 | 0.58 | 0.64 |
| 10-19 02:46 | +20 | ETH | UP | 0.48 | 0.81 | 3.01 |
| 10-19 02:46 | +15 | ETH | UP | 0.48 | 0.63 | 1.15 |
| 10-19 02:46 | +10 | ETH | UP | 0.48 | 0.58 | 0.64 |
| 10-19 02:46 | +5 | ETH | UP | 0.48 | 0.55 | 0.34 |
| 10-19 02:46 | +10 stop | NEAR | DOWN | 0.56 | 0.41 | -1.85 |
| 10-19 02:46 | +20 | NEAR | DOWN | 0.56 | 0.76 | 1.69 |
| 10-19 02:46 | +15 | NEAR | DOWN | 0.56 | 0.76 | 1.69 |
| 10-19 02:46 | +10 | NEAR | DOWN | 0.56 | 0.67 | 0.76 |
| 10-19 02:46 | +5 | NEAR | DOWN | 0.56 | 0.67 | 0.76 |
| 10-19 02:46 | +10 stop | BTC | UP | 0.61 | 0.76 | 1.20 |
| 10-19 02:46 | +20 | BTC | UP | 0.61 | 0.89 | 2.56 |
| 10-19 02:46 | +15 | BTC | UP | 0.61 | 0.76 | 1.20 |
| 10-19 02:46 | +10 | BTC | UP | 0.61 | 0.76 | 1.20 |
| 10-19 02:46 | +5 | BTC | UP | 0.61 | 0.70 | 0.58 |
