# Range-Scalp Bot

*Updated Sat Oct 10 19:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10770 | 9283 | 1487 (22) | 6 | $-3689.23 | -5.4% |
| **+10¢** | 8154 | 6422 | 1732 (36) | 5 | $-3521.88 | -6.9% |
| **+15¢** | 6876 | 5043 | 1833 (52) | 7 | $-2980.75 | -6.9% |
| **+20¢** | 6113 | 4203 | 1910 (66) | 7 | $-2548.13 | -6.6% |
| **+10¢ (15¢ stop)** | 13251 | 13210 | 41 (25) | 2 | $-5312.77 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 19:09 | +10 stop | SOL | UP | 0.53 | 0.63 | 0.65 |
| 10-10 19:09 | +10 | SOL | UP | 0.53 | 0.63 | 0.65 |
| 10-10 19:07 | +5 | SOL | DOWN | 0.71 | open |  |
| 10-10 19:07 | +10 stop | BTC | DOWN | 0.71 | open |  |
| 10-10 19:07 | +10 stop | ETH | UP | 0.59 | 0.73 | 1.09 |
| 10-10 19:06 | +10 stop | DOGE | DOWN | 0.66 | 0.50 | -1.94 |
| 10-10 19:06 | +10 stop | XRP | DOWN | 0.65 | 0.49 | -1.91 |
| 10-10 19:06 | +5 | XRP | DOWN | 0.65 | open |  |
| 10-10 19:06 | +10 stop | SOL | DOWN | 0.63 | 0.47 | -1.98 |
| 10-10 19:06 | +10 stop | ZEC | UP | 0.56 | open |  |
| 10-10 19:05 | +10 stop | DOGE | UP | 0.62 | 0.33 | -3.23 |
| 10-10 19:05 | +10 stop | ETH | UP | 0.68 | 0.52 | -1.94 |
| 10-10 19:05 | +15 | ETH | UP | 0.68 | open |  |
| 10-10 19:05 | +10 | ETH | UP | 0.68 | 0.79 | 0.82 |
| 10-10 19:05 | +5 | ETH | UP | 0.68 | 0.73 | 0.20 |
| 10-10 19:04 | +10 stop | ZEC | DOWN | 0.54 | 0.39 | -1.85 |
| 10-10 19:04 | +10 stop | BNB | UP | 0.70 | 0.82 | 0.94 |
| 10-10 19:04 | +5 | DOGE | UP | 0.62 | open |  |
| 10-10 19:04 | +5 | BTC | UP | 0.58 | open |  |
| 10-10 19:03 | +5 | DOGE | UP | 0.59 | 0.65 | 0.27 |
| 10-10 19:03 | +5 | ETH | UP | 0.69 | 0.76 | 0.42 |
| 10-10 19:03 | +10 stop | BTC | UP | 0.52 | 0.33 | -2.24 |
| 10-10 19:03 | +20 | BTC | UP | 0.52 | open |  |
| 10-10 19:03 | +15 | BTC | UP | 0.52 | open |  |
| 10-10 19:03 | +10 | BTC | UP | 0.52 | open |  |
| 10-10 19:03 | +5 | BTC | UP | 0.52 | 0.59 | 0.35 |
| 10-10 19:03 | +10 stop | XRP | UP | 0.64 | 0.47 | -2.05 |
| 10-10 19:03 | +20 | XRP | UP | 0.64 | open |  |
| 10-10 19:03 | +15 | XRP | UP | 0.64 | open |  |
| 10-10 19:03 | +10 | XRP | UP | 0.64 | open |  |
| 10-10 19:03 | +5 | XRP | UP | 0.64 | 0.71 | 0.38 |
| 10-10 19:02 | +10 stop | DOGE | UP | 0.58 | 0.43 | -1.86 |
| 10-10 19:02 | +20 | DOGE | UP | 0.58 | open |  |
| 10-10 19:02 | +15 | DOGE | UP | 0.58 | open |  |
| 10-10 19:02 | +10 | DOGE | UP | 0.58 | open |  |
| 10-10 19:02 | +5 | DOGE | UP | 0.58 | 0.66 | 0.46 |
| 10-10 19:02 | +10 stop | ETH | UP | 0.62 | 0.76 | 1.14 |
| 10-10 19:02 | +20 | ETH | UP | 0.62 | open |  |
| 10-10 19:02 | +15 | ETH | UP | 0.61 | 0.76 | 1.20 |
| 10-10 19:02 | +10 | ETH | UP | 0.61 | 0.71 | 0.68 |
