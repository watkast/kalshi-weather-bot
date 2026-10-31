# Range-Scalp Bot

*Updated Sat Oct 31 23:42 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42900 | 37407 | 5493 (62) | 4 | $-12104.35 | -4.5% |
| **+10¢** | 31987 | 25635 | 6352 (84) | 6 | $-10858.51 | -5.4% |
| **+15¢** | 26760 | 19910 | 6850 (112) | 5 | $-9951.25 | -5.9% |
| **+20¢** | 23767 | 16588 | 7179 (145) | 6 | $-8810.52 | -5.9% |
| **+10¢ (15¢ stop)** | 52327 | 52244 | 83 (48) | 1 | $-19827.00 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 23:41 | +10 stop | XRP | DOWN | 0.71 | 0.33 | -4.08 |
| 10-31 23:40 | +5 | BTC | DOWN | 0.71 | open |  |
| 10-31 23:40 | +10 stop | BTC | DOWN | 0.71 | open |  |
| 10-31 23:39 | +10 stop | XRP | DOWN | 0.71 | 0.84 | 1.05 |
| 10-31 23:38 | +10 stop | SOL | DOWN | 0.66 | 0.78 | 0.91 |
| 10-31 23:37 | +10 stop | XRP | UP | 0.60 | 0.37 | -2.64 |
| 10-31 23:37 | +5 | XRP | UP | 0.60 | 0.65 | 0.17 |
| 10-31 23:37 | +10 stop | BTC | UP | 0.61 | 0.46 | -1.85 |
| 10-31 23:37 | +10 stop | SOL | UP | 0.56 | 0.36 | -2.35 |
| 10-31 23:37 | +10 | SOL | UP | 0.57 | open |  |
| 10-31 23:37 | +5 | SOL | UP | 0.57 | open |  |
| 10-31 23:35 | +5 | XRP | UP | 0.55 | 0.68 | 0.96 |
| 10-31 23:34 | +5 | ZEC | UP | 0.70 | 0.81 | 0.84 |
| 10-31 23:33 | +10 stop | ETH | UP | 0.70 | 0.42 | -3.13 |
| 10-31 23:33 | +10 | ETH | UP | 0.70 | open |  |
| 10-31 23:33 | +5 | ETH | UP | 0.70 | 0.78 | 0.52 |
| 10-31 23:33 | +10 stop | NEAR | UP | 0.65 | 0.78 | 1.01 |
| 10-31 23:33 | +10 stop | XRP | UP | 0.64 | 0.48 | -1.95 |
| 10-31 23:33 | +10 | XRP | UP | 0.64 | open |  |
| 10-31 23:33 | +5 | XRP | UP | 0.64 | 0.69 | 0.18 |
| 10-31 23:33 | +10 stop | BNB | UP | 0.68 | 0.82 | 1.15 |
| 10-31 23:33 | +20 | BNB | UP | 0.68 | 0.88 | 1.78 |
| 10-31 23:33 | +15 | BNB | UP | 0.68 | 0.86 | 1.57 |
| 10-31 23:33 | +10 | BNB | UP | 0.68 | 0.82 | 1.15 |
| 10-31 23:33 | +5 | BNB | UP | 0.68 | 0.73 | 0.22 |
| 10-31 23:31 | +10 stop | BTC | DOWN | 0.64 | 0.46 | -2.15 |
| 10-31 23:31 | +20 | BTC | DOWN | 0.64 | open |  |
| 10-31 23:31 | +15 | BTC | DOWN | 0.64 | open |  |
| 10-31 23:31 | +10 | BTC | DOWN | 0.64 | open |  |
| 10-31 23:31 | +5 | BTC | DOWN | 0.64 | 0.71 | 0.38 |
| 10-31 23:31 | +10 stop | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-31 23:31 | +20 | DOGE | UP | 0.67 | 0.91 | 2.15 |
| 10-31 23:31 | +15 | DOGE | UP | 0.67 | 0.83 | 1.34 |
| 10-31 23:31 | +10 | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-31 23:31 | +5 | DOGE | UP | 0.67 | 0.77 | 0.71 |
| 10-31 23:31 | +10 stop | ZEC | UP | 0.67 | 0.81 | 1.13 |
| 10-31 23:31 | +20 | ZEC | UP | 0.67 | 0.88 | 1.86 |
| 10-31 23:31 | +15 | ZEC | UP | 0.67 | 0.85 | 1.55 |
| 10-31 23:31 | +10 | ZEC | UP | 0.67 | 0.81 | 1.13 |
| 10-31 23:31 | +5 | ZEC | UP | 0.67 | 0.73 | 0.30 |
