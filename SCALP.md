# Range-Scalp Bot

*Updated Sat Oct 24 09:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31803 | 27727 | 4076 (40) | 0 | $-9104.50 | -4.5% |
| **+10¢** | 23784 | 19074 | 4710 (58) | 2 | $-8092.68 | -5.4% |
| **+15¢** | 19908 | 14846 | 5062 (81) | 2 | $-7214.72 | -5.8% |
| **+20¢** | 17639 | 12339 | 5300 (103) | 2 | $-6397.78 | -5.8% |
| **+10¢ (15¢ stop)** | 39061 | 39002 | 59 (32) | 0 | $-14923.83 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-24 09:24 | +10 stop | HYPE | DOWN | 0.55 | 0.82 | 2.41 |
| 10-24 09:24 | +10 | HYPE | DOWN | 0.55 | 0.82 | 2.41 |
| 10-24 09:24 | +5 | HYPE | DOWN | 0.55 | 0.61 | 0.25 |
| 10-24 09:19 | +10 stop | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-24 09:19 | +20 | HYPE | DOWN | 0.68 | 0.91 | 2.09 |
| 10-24 09:19 | +15 | HYPE | DOWN | 0.68 | 0.86 | 1.55 |
| 10-24 09:19 | +10 | HYPE | DOWN | 0.68 | 0.81 | 1.03 |
| 10-24 09:19 | +5 | HYPE | DOWN | 0.69 | 0.76 | 0.42 |
| 10-24 09:18 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 10-24 09:17 | +10 stop | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 10-24 09:17 | +10 stop | SOL | DOWN | 0.59 | 0.76 | 1.40 |
| 10-24 09:17 | +5 | SOL | DOWN | 0.59 | 0.64 | 0.16 |
| 10-24 09:16 | +10 stop | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 10-24 09:16 | +20 | DOGE | DOWN | 0.63 | 0.85 | 1.94 |
| 10-24 09:16 | +15 | DOGE | DOWN | 0.63 | 0.85 | 1.94 |
| 10-24 09:16 | +10 | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 10-24 09:16 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 10-24 09:16 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.17 |
| 10-24 09:16 | +10 stop | NEAR | DOWN | 0.63 | 0.75 | 0.89 |
| 10-24 09:16 | +20 | NEAR | DOWN | 0.63 | 0.83 | 1.73 |
| 10-24 09:16 | +15 | NEAR | DOWN | 0.63 | 0.79 | 1.31 |
| 10-24 09:16 | +10 | NEAR | DOWN | 0.63 | 0.75 | 0.89 |
| 10-24 09:16 | +5 | NEAR | DOWN | 0.63 | 0.75 | 0.89 |
| 10-24 09:16 | +10 stop | BTC | DOWN | 0.68 | 0.82 | 1.13 |
| 10-24 09:16 | +20 | BTC | DOWN | 0.68 | 0.88 | 1.76 |
| 10-24 09:16 | +15 | BTC | DOWN | 0.68 | 0.84 | 1.34 |
| 10-24 09:16 | +10 | BTC | DOWN | 0.68 | 0.82 | 1.13 |
| 10-24 09:16 | +5 | BTC | DOWN | 0.68 | 0.75 | 0.40 |
| 10-24 09:16 | +10 stop | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 10-24 09:16 | +20 | XRP | DOWN | 0.69 | 0.91 | 2.00 |
| 10-24 09:16 | +15 | XRP | DOWN | 0.69 | 0.87 | 1.57 |
| 10-24 09:16 | +10 | XRP | DOWN | 0.69 | 0.79 | 0.73 |
| 10-24 09:16 | +5 | XRP | DOWN | 0.69 | 0.77 | 0.52 |
| 10-24 09:16 | +10 stop | BNB | DOWN | 0.69 | 0.84 | 1.25 |
| 10-24 09:16 | +20 | BNB | DOWN | 0.69 | 0.95 | 2.42 |
| 10-24 09:16 | +15 | BNB | DOWN | 0.69 | 0.84 | 1.25 |
| 10-24 09:16 | +10 | BNB | DOWN | 0.68 | 0.84 | 1.30 |
| 10-24 09:16 | +5 | BNB | DOWN | 0.68 | 0.74 | 0.26 |
| 10-24 09:16 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 10-24 09:16 | +20 | ETH | DOWN | 0.71 | 0.94 | 2.14 |
