# Range-Scalp Bot

*Updated Fri Oct 09 02:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8402 | 7276 | 1126 (13) | 7 | $-2683.01 | -5.1% |
| **+10¢** | 6364 | 5033 | 1331 (25) | 8 | $-2631.00 | -6.6% |
| **+15¢** | 5368 | 3967 | 1401 (37) | 9 | $-2114.76 | -6.3% |
| **+20¢** | 4774 | 3320 | 1454 (45) | 9 | $-1736.68 | -5.8% |
| **+10¢ (15¢ stop)** | 10216 | 10186 | 30 (19) | 0 | $-3746.85 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 02:39 | +10 stop | NEAR | DOWN | 0.60 | 0.22 | -4.10 |
| 10-09 02:39 | +10 stop | XRP | DOWN | 0.49 | 0.26 | -2.62 |
| 10-09 02:39 | +10 stop | XRP | UP | 0.41 | 0.54 | 0.92 |
| 10-09 02:38 | +10 stop | XRP | UP | 0.48 | 0.62 | 1.05 |
| 10-09 02:38 | +10 stop | NEAR | DOWN | 0.69 | 0.53 | -1.93 |
| 10-09 02:37 | +5 | DOGE | DOWN | 0.60 | 0.69 | 0.58 |
| 10-09 02:36 | +10 stop | NEAR | UP | 0.63 | 0.39 | -2.76 |
| 10-09 02:36 | +5 | DOGE | DOWN | 0.60 | 0.72 | 0.88 |
| 10-09 02:34 | +10 stop | ZEC | DOWN | 0.62 | 0.46 | -1.95 |
| 10-09 02:34 | +10 stop | BNB | DOWN | 0.62 | 0.46 | -1.95 |
| 10-09 02:34 | +10 stop | HYPE | UP | 0.63 | 0.82 | 1.62 |
| 10-09 02:34 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.69 |
| 10-09 02:34 | +5 | SOL | UP | 0.64 | 0.73 | 0.59 |
| 10-09 02:34 | +10 stop | ETH | UP | 0.58 | 0.68 | 0.66 |
| 10-09 02:33 | +10 stop | NEAR | UP | 0.53 | 0.65 | 0.88 |
| 10-09 02:33 | +10 stop | BTC | UP | 0.59 | 0.73 | 1.09 |
| 10-09 02:33 | +5 | SOL | UP | 0.56 | 0.62 | 0.25 |
| 10-09 02:32 | +10 stop | ZEC | DOWN | 0.68 | 0.48 | -2.34 |
| 10-09 02:32 | +20 | ZEC | DOWN | 0.68 | open |  |
| 10-09 02:32 | +15 | ZEC | DOWN | 0.68 | open |  |
| 10-09 02:32 | +10 | ZEC | DOWN | 0.68 | open |  |
| 10-09 02:32 | +5 | ZEC | DOWN | 0.68 | open |  |
| 10-09 02:31 | +10 stop | BTC | DOWN | 0.53 | 0.37 | -1.95 |
| 10-09 02:31 | +20 | BTC | DOWN | 0.53 | open |  |
| 10-09 02:31 | +15 | BTC | DOWN | 0.53 | open |  |
| 10-09 02:31 | +10 | BTC | DOWN | 0.53 | open |  |
| 10-09 02:31 | +5 | BTC | DOWN | 0.53 | open |  |
| 10-09 02:31 | +10 stop | ETH | DOWN | 0.59 | 0.43 | -1.95 |
| 10-09 02:31 | +20 | ETH | DOWN | 0.59 | open |  |
| 10-09 02:31 | +15 | ETH | DOWN | 0.59 | open |  |
| 10-09 02:31 | +10 | ETH | DOWN | 0.59 | open |  |
| 10-09 02:31 | +5 | ETH | DOWN | 0.59 | open |  |
| 10-09 02:31 | +10 stop | SOL | DOWN | 0.54 | 0.37 | -2.05 |
| 10-09 02:31 | +20 | SOL | DOWN | 0.54 | open |  |
| 10-09 02:31 | +15 | SOL | DOWN | 0.54 | open |  |
| 10-09 02:31 | +10 | SOL | DOWN | 0.54 | open |  |
| 10-09 02:31 | +5 | SOL | DOWN | 0.54 | 0.60 | 0.25 |
| 10-09 02:31 | +10 stop | BNB | DOWN | 0.70 | 0.52 | -2.17 |
| 10-09 02:31 | +20 | BNB | DOWN | 0.70 | open |  |
| 10-09 02:31 | +15 | BNB | DOWN | 0.70 | open |  |
