# Range-Scalp Bot

*Updated Wed Oct 28 02:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 37431 | 32677 | 4754 (45) | 7 | $-10426.85 | -4.4% |
| **+10¢** | 27948 | 22443 | 5505 (67) | 7 | $-9292.74 | -5.3% |
| **+15¢** | 23383 | 17471 | 5912 (91) | 7 | $-8252.89 | -5.6% |
| **+20¢** | 20725 | 14538 | 6187 (116) | 8 | $-7214.71 | -5.5% |
| **+10¢ (15¢ stop)** | 45854 | 45789 | 65 (34) | 1 | $-17473.83 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 02:26 | +10 stop | XRP | DOWN | 0.40 | open |  |
| 10-28 02:26 | +20 | XRP | DOWN | 0.41 | open |  |
| 10-28 02:26 | +15 | XRP | DOWN | 0.43 | open |  |
| 10-28 02:26 | +10 | XRP | DOWN | 0.41 | open |  |
| 10-28 02:26 | +5 | XRP | DOWN | 0.39 | open |  |
| 10-28 02:25 | +10 stop | BNB | UP | 0.59 | 0.43 | -1.95 |
| 10-28 02:25 | +10 | BNB | UP | 0.59 | open |  |
| 10-28 02:25 | +10 stop | DOGE | UP | 0.59 | 0.36 | -2.64 |
| 10-28 02:25 | +10 | DOGE | UP | 0.59 | open |  |
| 10-28 02:25 | +5 | DOGE | UP | 0.59 | open |  |
| 10-28 02:25 | +5 | BNB | UP | 0.63 | open |  |
| 10-28 02:25 | +10 stop | ETH | DOWN | 0.55 | 0.73 | 1.48 |
| 10-28 02:24 | +10 stop | DOGE | UP | 0.53 | 0.64 | 0.75 |
| 10-28 02:24 | +20 | DOGE | UP | 0.53 | open |  |
| 10-28 02:24 | +15 | DOGE | UP | 0.53 | open |  |
| 10-28 02:24 | +10 | DOGE | UP | 0.53 | 0.64 | 0.75 |
| 10-28 02:24 | +5 | DOGE | UP | 0.53 | 0.64 | 0.75 |
| 10-28 02:24 | +10 stop | BNB | UP | 0.48 | 0.66 | 1.46 |
| 10-28 02:24 | +10 | BNB | UP | 0.48 | 0.66 | 1.46 |
| 10-28 02:24 | +5 | BNB | UP | 0.48 | 0.56 | 0.44 |
| 10-28 02:23 | +10 stop | BTC | DOWN | 0.64 | 0.78 | 1.10 |
| 10-28 02:23 | +10 stop | SOL | DOWN | 0.58 | 0.70 | 0.87 |
| 10-28 02:23 | +5 | ETH | UP | 0.68 | open |  |
| 10-28 02:22 | +10 stop | ZEC | UP | 0.63 | 0.75 | 0.89 |
| 10-28 02:22 | +10 stop | BTC | DOWN | 0.54 | 0.64 | 0.65 |
| 10-28 02:22 | +10 stop | ETH | UP | 0.66 | 0.51 | -1.84 |
| 10-28 02:22 | +20 | ETH | UP | 0.66 | open |  |
| 10-28 02:22 | +15 | ETH | UP | 0.66 | open |  |
| 10-28 02:22 | +10 | ETH | UP | 0.66 | open |  |
| 10-28 02:22 | +5 | ETH | UP | 0.66 | 0.72 | 0.29 |
| 10-28 02:22 | +10 stop | BNB | UP | 0.59 | 0.69 | 0.68 |
| 10-28 02:22 | +20 | BNB | UP | 0.59 | open |  |
| 10-28 02:22 | +15 | BNB | UP | 0.59 | open |  |
| 10-28 02:22 | +10 | BNB | UP | 0.59 | 0.69 | 0.68 |
| 10-28 02:22 | +5 | BNB | UP | 0.59 | 0.64 | 0.16 |
| 10-28 02:21 | +10 stop | NEAR | DOWN | 0.61 | 0.73 | 0.86 |
| 10-28 02:21 | +10 stop | ZEC | UP | 0.64 | 0.45 | -2.25 |
| 10-28 02:21 | +20 | ZEC | UP | 0.64 | open |  |
| 10-28 02:21 | +15 | ZEC | UP | 0.64 | 0.79 | 1.21 |
| 10-28 02:21 | +10 | ZEC | UP | 0.64 | 0.75 | 0.79 |
