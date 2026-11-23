# Range-Scalp Bot

*Updated Mon Nov 23 04:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69636 | 60766 | 8870 (146) | 2 | $-18715.51 | -4.3% |
| **+10¢** | 51958 | 41596 | 10362 (189) | 3 | $-17402.78 | -5.3% |
| **+15¢** | 43539 | 32375 | 11164 (244) | 3 | $-15553.75 | -5.7% |
| **+20¢** | 38774 | 27033 | 11741 (308) | 3 | $-13870.12 | -5.7% |
| **+10¢ (15¢ stop)** | 84790 | 84600 | 190 (118) | 0 | $-31177.73 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-23 04:56 | +5 | ETH | DOWN | 0.54 | 0.67 | 0.96 |
| 11-23 04:56 | +5 | BNB | DOWN | 0.42 | 0.60 | 1.45 |
| 11-23 04:55 | +5 | SOL | DOWN | 0.66 | open |  |
| 11-23 04:55 | +10 stop | SOL | DOWN | 0.68 | 0.25 | -4.60 |
| 11-23 04:55 | +10 stop | DOGE | DOWN | 0.69 | 0.49 | -2.33 |
| 11-23 04:55 | +10 | XRP | UP | 0.42 | 0.68 | 2.26 |
| 11-23 04:55 | +5 | XRP | UP | 0.58 | 0.68 | 0.66 |
| 11-23 04:55 | +10 stop | XRP | UP | 0.68 | 0.50 | -2.14 |
| 11-23 04:55 | +5 | ETH | DOWN | 0.59 | 0.68 | 0.57 |
| 11-23 04:54 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 11-23 04:54 | +10 stop | DOGE | DOWN | 0.67 | 0.50 | -2.04 |
| 11-23 04:54 | +10 stop | SOL | DOWN | 0.57 | 0.42 | -1.86 |
| 11-23 04:54 | +10 | SOL | DOWN | 0.56 | open |  |
| 11-23 04:54 | +5 | SOL | DOWN | 0.56 | 0.62 | 0.25 |
| 11-23 04:54 | +10 stop | BNB | DOWN | 0.57 | 0.29 | -3.13 |
| 11-23 04:54 | +5 | BNB | DOWN | 0.57 | 0.64 | 0.35 |
| 11-23 04:54 | +10 stop | ETH | DOWN | 0.64 | 0.42 | -2.55 |
| 11-23 04:54 | +15 | ETH | DOWN | 0.64 | open |  |
| 11-23 04:54 | +10 | ETH | DOWN | 0.64 | open |  |
| 11-23 04:54 | +5 | ETH | DOWN | 0.61 | 0.67 | 0.27 |
| 11-23 04:53 | +10 stop | XRP | DOWN | 0.62 | 0.44 | -2.12 |
| 11-23 04:53 | +10 stop | HYPE | DOWN | 0.58 | 0.30 | -3.13 |
| 11-23 04:53 | +20 | SOL | DOWN | 0.71 | open |  |
| 11-23 04:52 | +10 stop | ZEC | UP | 0.71 | 0.87 | 1.37 |
| 11-23 04:52 | +20 | ZEC | UP | 0.71 | 0.94 | 2.16 |
| 11-23 04:52 | +15 | ZEC | UP | 0.71 | 0.87 | 1.37 |
| 11-23 04:52 | +10 | ZEC | UP | 0.71 | 0.87 | 1.37 |
| 11-23 04:52 | +5 | ZEC | UP | 0.71 | 0.78 | 0.42 |
| 11-23 04:51 | +10 stop | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 11-23 04:51 | +10 stop | HYPE | UP | 0.70 | 0.54 | -1.93 |
| 11-23 04:51 | +15 | HYPE | UP | 0.70 | 0.88 | 1.57 |
| 11-23 04:51 | +10 | HYPE | UP | 0.70 | 0.84 | 1.15 |
| 11-23 04:51 | +5 | HYPE | UP | 0.70 | 0.84 | 1.15 |
| 11-23 04:50 | +5 | BTC | UP | 0.57 | 0.63 | 0.25 |
| 11-23 04:50 | +10 stop | BTC | UP | 0.57 | 0.73 | 1.28 |
| 11-23 04:50 | +10 stop | ETH | DOWN | 0.62 | 0.72 | 0.68 |
| 11-23 04:50 | +5 | ETH | DOWN | 0.62 | 0.70 | 0.48 |
| 11-23 04:50 | +10 stop | BTC | DOWN | 0.44 | 0.54 | 0.64 |
| 11-23 04:49 | +10 stop | NEAR | DOWN | 0.65 | 0.79 | 1.09 |
| 11-23 04:48 | +10 stop | HYPE | UP | 0.57 | 0.68 | 0.79 |
