# Range-Scalp Bot

*Updated Sat Oct 10 02:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 9808 | 8462 | 1346 (18) | 5 | $-3325.78 | -5.4% |
| **+10¢** | 7409 | 5837 | 1572 (30) | 4 | $-3213.21 | -6.9% |
| **+15¢** | 6248 | 4590 | 1658 (43) | 4 | $-2682.76 | -6.8% |
| **+20¢** | 5554 | 3829 | 1725 (55) | 7 | $-2270.34 | -6.5% |
| **+10¢ (15¢ stop)** | 12038 | 12003 | 35 (22) | 0 | $-4679.16 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 02:10 | +10 stop | ETH | DOWN | 0.40 | 0.69 | 2.58 |
| 10-10 02:10 | +15 | ETH | DOWN | 0.40 | 0.69 | 2.58 |
| 10-10 02:10 | +10 | ETH | DOWN | 0.40 | 0.69 | 2.58 |
| 10-10 02:10 | +5 | ETH | DOWN | 0.39 | 0.69 | 2.64 |
| 10-10 02:09 | +10 stop | SOL | DOWN | 0.70 | 0.43 | -3.01 |
| 10-10 02:09 | +10 stop | BTC | DOWN | 0.58 | 0.30 | -3.13 |
| 10-10 02:09 | +10 stop | XRP | UP | 0.61 | 0.80 | 1.61 |
| 10-10 02:07 | +5 | BNB | DOWN | 0.64 | open |  |
| 10-10 02:07 | +10 stop | XRP | DOWN | 0.64 | 0.25 | -4.18 |
| 10-10 02:07 | +10 | XRP | DOWN | 0.63 | open |  |
| 10-10 02:07 | +5 | XRP | DOWN | 0.64 | open |  |
| 10-10 02:06 | +10 stop | XRP | DOWN | 0.55 | 0.67 | 0.89 |
| 10-10 02:06 | +15 | XRP | DOWN | 0.55 | open |  |
| 10-10 02:06 | +10 | XRP | DOWN | 0.55 | 0.67 | 0.89 |
| 10-10 02:06 | +5 | XRP | DOWN | 0.55 | 0.64 | 0.58 |
| 10-10 02:05 | +10 stop | BTC | DOWN | 0.64 | 0.47 | -2.05 |
| 10-10 02:05 | +10 stop | SOL | DOWN | 0.59 | 0.71 | 0.83 |
| 10-10 02:04 | +5 | BNB | DOWN | 0.67 | 0.72 | 0.19 |
| 10-10 02:04 | +10 stop | NEAR | DOWN | 0.66 | 0.81 | 1.24 |
| 10-10 02:04 | +10 stop | ZEC | DOWN | 0.65 | 0.81 | 1.34 |
| 10-10 02:04 | +10 stop | DOGE | UP | 0.52 | 0.34 | -2.14 |
| 10-10 02:04 | +10 stop | BTC | UP | 0.61 | 0.31 | -3.32 |
| 10-10 02:03 | +10 stop | BNB | DOWN | 0.63 | 0.25 | -4.11 |
| 10-10 02:03 | +20 | BNB | DOWN | 0.63 | open |  |
| 10-10 02:03 | +15 | BNB | DOWN | 0.63 | open |  |
| 10-10 02:03 | +10 | BNB | DOWN | 0.63 | open |  |
| 10-10 02:03 | +5 | BNB | DOWN | 0.63 | 0.69 | 0.28 |
| 10-10 02:03 | +5 | XRP | DOWN | 0.58 | 0.66 | 0.44 |
| 10-10 02:03 | +10 stop | NEAR | UP | 0.66 | 0.47 | -2.19 |
| 10-10 02:03 | +5 | NEAR | UP | 0.66 | open |  |
| 10-10 02:03 | +10 stop | SOL | UP | 0.60 | 0.44 | -1.91 |
| 10-10 02:03 | +20 | SOL | UP | 0.60 | open |  |
| 10-10 02:03 | +15 | SOL | UP | 0.60 | open |  |
| 10-10 02:03 | +10 | SOL | UP | 0.58 | open |  |
| 10-10 02:03 | +5 | SOL | UP | 0.58 | open |  |
| 10-10 02:03 | +10 stop | ZEC | UP | 0.57 | 0.40 | -2.05 |
| 10-10 02:03 | +5 | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 10-10 02:03 | +10 stop | DOGE | DOWN | 0.59 | 0.42 | -2.05 |
| 10-10 02:03 | +20 | DOGE | DOWN | 0.59 | open |  |
| 10-10 02:03 | +15 | DOGE | DOWN | 0.62 | 0.77 | 1.20 |
