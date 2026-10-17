# Range-Scalp Bot

*Updated Sat Oct 17 20:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21520 | 18756 | 2764 (29) | 0 | $-6116.61 | -4.5% |
| **+10¢** | 16178 | 12979 | 3199 (41) | 1 | $-5470.78 | -5.4% |
| **+15¢** | 13527 | 10077 | 3450 (61) | 1 | $-4967.83 | -5.9% |
| **+20¢** | 11979 | 8364 | 3615 (80) | 1 | $-4420.38 | -5.9% |
| **+10¢ (15¢ stop)** | 26412 | 26362 | 50 (29) | 1 | $-10051.44 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 20:15 | +10 stop | BTC | UP | 0.45 | open |  |
| 10-17 20:15 | +20 | BTC | UP | 0.45 | open |  |
| 10-17 20:15 | +15 | BTC | UP | 0.45 | open |  |
| 10-17 20:15 | +10 | BTC | UP | 0.45 | open |  |
| 10-17 20:15 | +5 | BTC | UP | 0.45 | 0.50 | 0.14 |
| 10-17 20:13 | +10 stop | BTC | UP | 0.65 | 0.76 | 0.84 |
| 10-17 20:13 | +15 | BTC | UP | 0.63 | 0.92 | 2.66 |
| 10-17 20:13 | +10 | BTC | UP | 0.62 | 0.76 | 1.10 |
| 10-17 20:13 | +5 | BTC | UP | 0.63 | 0.76 | 0.95 |
| 10-17 20:11 | +10 stop | BTC | UP | 0.65 | 0.78 | 1.01 |
| 10-17 20:11 | +20 | BTC | UP | 0.65 | 0.92 | 2.47 |
| 10-17 20:11 | +15 | BTC | UP | 0.65 | 0.82 | 1.43 |
| 10-17 20:11 | +10 | BTC | UP | 0.66 | 0.78 | 0.91 |
| 10-17 20:11 | +5 | BTC | UP | 0.66 | 0.78 | 0.91 |
| 10-17 20:11 | +5 | XRP | DOWN | 0.45 | 0.64 | 1.55 |
| 10-17 20:11 | +10 stop | BNB | DOWN | 0.62 | 0.44 | -2.15 |
| 10-17 20:11 | +15 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-17 20:11 | +10 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-17 20:11 | +5 | BNB | DOWN | 0.62 | yes | -6.37 |
| 10-17 20:11 | +10 stop | XRP | DOWN | 0.56 | 0.27 | -3.22 |
| 10-17 20:10 | +10 stop | SOL | UP | 0.38 | 0.56 | 1.45 |
| 10-17 20:10 | +15 | SOL | UP | 0.38 | 0.56 | 1.45 |
| 10-17 20:10 | +5 | SOL | UP | 0.38 | 0.56 | 1.45 |
| 10-17 20:08 | +10 stop | XRP | UP | 0.60 | 0.75 | 1.19 |
| 10-17 20:08 | +10 stop | SOL | DOWN | 0.61 | 0.76 | 1.20 |
| 10-17 20:07 | +5 | SOL | DOWN | 0.59 | 0.76 | 1.40 |
| 10-17 20:06 | +10 stop | XRP | UP | 0.62 | 0.73 | 0.79 |
| 10-17 20:06 | +10 | ETH | UP | 0.69 | 0.84 | 1.25 |
| 10-17 20:06 | +5 | ETH | UP | 0.69 | 0.77 | 0.52 |
| 10-17 20:06 | +5 | BTC | UP | 0.67 | 0.75 | 0.50 |
| 10-17 20:06 | +10 stop | ZEC | UP | 0.66 | 0.78 | 0.91 |
| 10-17 20:06 | +10 stop | ETH | UP | 0.71 | 0.84 | 1.05 |
| 10-17 20:06 | +20 | ETH | UP | 0.71 | 0.93 | 1.96 |
| 10-17 20:06 | +15 | ETH | UP | 0.71 | 0.88 | 1.47 |
| 10-17 20:06 | +10 stop | SOL | DOWN | 0.61 | 0.44 | -2.05 |
| 10-17 20:06 | +20 | SOL | DOWN | 0.61 | 0.97 | 3.44 |
| 10-17 20:06 | +15 | SOL | DOWN | 0.61 | 0.76 | 1.20 |
| 10-17 20:06 | +5 | SOL | DOWN | 0.61 | 0.67 | 0.27 |
| 10-17 20:06 | +10 stop | ZEC | DOWN | 0.42 | 0.61 | 1.55 |
| 10-17 20:06 | +10 stop | NEAR | DOWN | 0.40 | 0.56 | 1.25 |
