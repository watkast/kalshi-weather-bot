# Range-Scalp Bot

*Updated Sun Oct 25 05:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 32617 | 28442 | 4175 (42) | 1 | $-9274.72 | -4.5% |
| **+10¢** | 24414 | 19578 | 4836 (60) | 1 | $-8307.26 | -5.4% |
| **+15¢** | 20440 | 15238 | 5202 (83) | 1 | $-7455.57 | -5.8% |
| **+20¢** | 18108 | 12664 | 5444 (105) | 1 | $-6594.35 | -5.8% |
| **+10¢ (15¢ stop)** | 40076 | 40016 | 60 (32) | 0 | $-15330.70 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-25 05:12 | +10 stop | ETH | DOWN | 0.63 | 0.47 | -1.95 |
| 10-25 05:10 | +10 stop | HYPE | DOWN | 0.68 | 0.53 | -1.84 |
| 10-25 05:10 | +15 | HYPE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-25 05:10 | +10 | HYPE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-25 05:10 | +5 | HYPE | DOWN | 0.68 | 0.74 | 0.30 |
| 10-25 05:07 | +5 | BTC | DOWN | 0.69 | 0.76 | 0.42 |
| 10-25 05:06 | +5 | BTC | DOWN | 0.61 | 0.69 | 0.48 |
| 10-25 05:06 | +10 stop | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-25 05:06 | +10 stop | HYPE | DOWN | 0.71 | 0.86 | 1.27 |
| 10-25 05:05 | +10 stop | NEAR | DOWN | 0.62 | 0.74 | 0.89 |
| 10-25 05:05 | +5 | ZEC | DOWN | 0.69 | 0.83 | 1.18 |
| 10-25 05:04 | +5 | ZEC | DOWN | 0.58 | 0.63 | 0.15 |
| 10-25 05:04 | +5 | ZEC | DOWN | 0.56 | 0.62 | 0.25 |
| 10-25 05:03 | +10 stop | NEAR | DOWN | 0.51 | 0.63 | 0.85 |
| 10-25 05:03 | +10 stop | BNB | UP | 0.65 | 0.37 | -3.13 |
| 10-25 05:03 | +10 stop | BTC | DOWN | 0.62 | 0.44 | -2.15 |
| 10-25 05:03 | +20 | BTC | DOWN | 0.62 | 0.84 | 1.93 |
| 10-25 05:03 | +15 | BTC | DOWN | 0.62 | 0.78 | 1.30 |
| 10-25 05:03 | +10 | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-25 05:03 | +5 | BTC | DOWN | 0.61 | 0.67 | 0.27 |
| 10-25 05:03 | +5 | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 10-25 05:02 | +10 stop | ETH | DOWN | 0.70 | 0.47 | -2.63 |
| 10-25 05:02 | +10 stop | NEAR | DOWN | 0.67 | 0.50 | -2.04 |
| 10-25 05:02 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 10-25 05:02 | +15 | NEAR | DOWN | 0.67 | 0.85 | 1.55 |
| 10-25 05:02 | +10 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 10-25 05:02 | +5 | NEAR | DOWN | 0.67 | 0.74 | 0.40 |
| 10-25 05:02 | +10 stop | HYPE | DOWN | 0.70 | 0.53 | -2.03 |
| 10-25 05:02 | +20 | HYPE | DOWN | 0.70 | 0.93 | 2.14 |
| 10-25 05:02 | +15 | HYPE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-25 05:02 | +10 | HYPE | DOWN | 0.70 | 0.86 | 1.36 |
| 10-25 05:02 | +5 | HYPE | DOWN | 0.70 | 0.75 | 0.21 |
| 10-25 05:01 | +10 stop | SOL | DOWN | 0.68 | 0.78 | 0.73 |
| 10-25 05:01 | +20 | SOL | DOWN | 0.68 | 0.91 | 2.07 |
| 10-25 05:01 | +15 | SOL | DOWN | 0.68 | 0.85 | 1.47 |
| 10-25 05:01 | +10 | SOL | DOWN | 0.68 | 0.78 | 0.73 |
| 10-25 05:01 | +5 | SOL | DOWN | 0.68 | 0.73 | 0.22 |
| 10-25 05:01 | +10 stop | XRP | DOWN | 0.59 | 0.75 | 1.27 |
| 10-25 05:01 | +5 | XRP | DOWN | 0.59 | 0.75 | 1.29 |
| 10-25 05:01 | +10 stop | ZEC | DOWN | 0.57 | 0.83 | 2.32 |
