# Range-Scalp Bot

*Updated Sat Oct 31 07:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41939 | 36592 | 5347 (54) | 2 | $-11786.41 | -4.5% |
| **+10¢** | 31258 | 25066 | 6192 (78) | 4 | $-10564.76 | -5.4% |
| **+15¢** | 26130 | 19454 | 6676 (106) | 4 | $-9659.77 | -5.9% |
| **+20¢** | 23204 | 16214 | 6990 (137) | 4 | $-8502.83 | -5.8% |
| **+10¢ (15¢ stop)** | 51118 | 51043 | 75 (41) | 1 | $-19282.53 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 07:09 | +10 stop | BTC | UP | 0.70 | open |  |
| 10-31 07:09 | +10 | BTC | UP | 0.70 | open |  |
| 10-31 07:09 | +5 | BTC | UP | 0.69 | 0.74 | 0.21 |
| 10-31 07:09 | +10 stop | NEAR | DOWN | 0.59 | 0.38 | -2.44 |
| 10-31 07:08 | +10 stop | ETH | DOWN | 0.62 | 0.78 | 1.30 |
| 10-31 07:08 | +20 | ETH | DOWN | 0.62 | 0.83 | 1.83 |
| 10-31 07:08 | +15 | ETH | DOWN | 0.62 | 0.78 | 1.30 |
| 10-31 07:08 | +10 | ETH | DOWN | 0.62 | 0.78 | 1.30 |
| 10-31 07:08 | +5 | ETH | DOWN | 0.62 | 0.69 | 0.38 |
| 10-31 07:07 | +10 stop | BNB | UP | 0.58 | 0.27 | -3.42 |
| 10-31 07:07 | +10 stop | BTC | UP | 0.70 | 0.81 | 0.84 |
| 10-31 07:07 | +20 | BTC | UP | 0.70 | open |  |
| 10-31 07:07 | +15 | BTC | UP | 0.70 | open |  |
| 10-31 07:07 | +10 | BTC | UP | 0.69 | 0.81 | 0.94 |
| 10-31 07:07 | +5 | BTC | UP | 0.69 | 0.81 | 0.94 |
| 10-31 07:06 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 10-31 07:06 | +10 | ZEC | UP | 0.68 | 0.83 | 1.24 |
| 10-31 07:06 | +10 stop | ZEC | UP | 0.67 | 0.83 | 1.34 |
| 10-31 07:06 | +5 | ZEC | UP | 0.65 | 0.83 | 1.54 |
| 10-31 07:05 | +10 stop | BTC | UP | 0.63 | 0.74 | 0.79 |
| 10-31 07:05 | +10 | BTC | UP | 0.62 | 0.74 | 0.89 |
| 10-31 07:05 | +5 | BTC | UP | 0.62 | 0.74 | 0.89 |
| 10-31 07:05 | +10 stop | ETH | DOWN | 0.51 | 0.65 | 1.06 |
| 10-31 07:05 | +20 | ETH | DOWN | 0.52 | 0.76 | 2.09 |
| 10-31 07:05 | +15 | ETH | DOWN | 0.52 | 0.69 | 1.37 |
| 10-31 07:05 | +10 | ETH | DOWN | 0.52 | 0.65 | 0.96 |
| 10-31 07:05 | +5 | ETH | DOWN | 0.51 | 0.59 | 0.45 |
| 10-31 07:05 | +5 | BTC | UP | 0.55 | 0.65 | 0.66 |
| 10-31 07:05 | +10 stop | BTC | UP | 0.55 | 0.65 | 0.66 |
| 10-31 07:05 | +10 stop | NEAR | DOWN | 0.59 | 0.37 | -2.54 |
| 10-31 07:05 | +20 | NEAR | DOWN | 0.60 | open |  |
| 10-31 07:05 | +15 | NEAR | DOWN | 0.59 | open |  |
| 10-31 07:05 | +10 | NEAR | DOWN | 0.59 | open |  |
| 10-31 07:05 | +5 | NEAR | DOWN | 0.61 | open |  |
| 10-31 07:04 | +10 stop | BNB | DOWN | 0.67 | 0.50 | -2.04 |
| 10-31 07:04 | +5 | BNB | DOWN | 0.67 | 0.73 | 0.30 |
| 10-31 07:03 | +10 stop | BTC | DOWN | 0.69 | 0.50 | -2.23 |
| 10-31 07:02 | +10 stop | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 10-31 07:02 | +10 stop | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 10-31 07:01 | +10 stop | BNB | DOWN | 0.70 | 0.80 | 0.73 |
