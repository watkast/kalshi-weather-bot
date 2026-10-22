# Range-Scalp Bot

*Updated Thu Oct 22 06:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 28404 | 24753 | 3651 (39) | 4 | $-8152.49 | -4.6% |
| **+10¢** | 21309 | 17084 | 4225 (55) | 6 | $-7260.07 | -5.4% |
| **+15¢** | 17847 | 13302 | 4545 (78) | 8 | $-6488.93 | -5.8% |
| **+20¢** | 15789 | 11022 | 4767 (98) | 7 | $-5870.44 | -5.9% |
| **+10¢ (15¢ stop)** | 34835 | 34776 | 59 (32) | 3 | $-13070.79 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-22 06:06 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-22 06:06 | +15 | XRP | UP | 0.71 | open |  |
| 10-22 06:06 | +10 | XRP | UP | 0.71 | 0.81 | 0.74 |
| 10-22 06:06 | +5 | XRP | UP | 0.71 | 0.79 | 0.53 |
| 10-22 06:06 | +10 stop | SOL | DOWN | 0.61 | open |  |
| 10-22 06:06 | +10 stop | NEAR | DOWN | 0.63 | 0.46 | -2.05 |
| 10-22 06:06 | +10 stop | BTC | DOWN | 0.61 | open |  |
| 10-22 06:06 | +5 | DOGE | UP | 0.55 | 0.60 | 0.15 |
| 10-22 06:05 | +10 stop | DOGE | UP | 0.52 | open |  |
| 10-22 06:05 | +5 | DOGE | UP | 0.60 | 0.69 | 0.58 |
| 10-22 06:05 | +5 | ETH | DOWN | 0.42 | 0.57 | 1.14 |
| 10-22 06:05 | +10 stop | NEAR | DOWN | 0.45 | 0.55 | 0.65 |
| 10-22 06:05 | +5 | SOL | DOWN | 0.59 | open |  |
| 10-22 06:05 | +5 | DOGE | DOWN | 0.50 | 0.59 | 0.55 |
| 10-22 06:04 | +10 stop | HYPE | UP | 0.71 | 0.84 | 1.10 |
| 10-22 06:04 | +10 | NEAR | DOWN | 0.61 | open |  |
| 10-22 06:04 | +5 | NEAR | DOWN | 0.61 | open |  |
| 10-22 06:04 | +10 stop | DOGE | DOWN | 0.55 | 0.30 | -2.83 |
| 10-22 06:04 | +20 | DOGE | DOWN | 0.55 | open |  |
| 10-22 06:04 | +15 | DOGE | DOWN | 0.55 | open |  |
| 10-22 06:04 | +10 | DOGE | DOWN | 0.55 | open |  |
| 10-22 06:04 | +5 | DOGE | DOWN | 0.55 | 0.64 | 0.55 |
| 10-22 06:04 | +10 stop | XRP | UP | 0.56 | 0.76 | 1.69 |
| 10-22 06:04 | +15 | ETH | DOWN | 0.57 | open |  |
| 10-22 06:04 | +5 | ETH | DOWN | 0.57 | 0.62 | 0.15 |
| 10-22 06:04 | +10 stop | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-22 06:04 | +10 | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-22 06:04 | +5 | ZEC | DOWN | 0.67 | 0.75 | 0.50 |
| 10-22 06:03 | +10 stop | ETH | DOWN | 0.68 | 0.43 | -2.84 |
| 10-22 06:03 | +10 stop | BTC | DOWN | 0.66 | 0.50 | -1.94 |
| 10-22 06:03 | +10 | BTC | DOWN | 0.66 | open |  |
| 10-22 06:03 | +5 | BTC | DOWN | 0.67 | open |  |
| 10-22 06:03 | +10 stop | XRP | DOWN | 0.63 | 0.41 | -2.54 |
| 10-22 06:03 | +10 | ETH | DOWN | 0.65 | open |  |
| 10-22 06:03 | +10 stop | HYPE | DOWN | 0.56 | 0.39 | -2.05 |
| 10-22 06:03 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 10-22 06:03 | +5 | ETH | DOWN | 0.65 | 0.70 | 0.19 |
| 10-22 06:02 | +10 stop | BNB | UP | 0.58 | 0.73 | 1.18 |
| 10-22 06:02 | +10 | BNB | UP | 0.58 | 0.73 | 1.18 |
| 10-22 06:02 | +5 | BNB | UP | 0.58 | 0.66 | 0.46 |
