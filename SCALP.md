# Range-Scalp Bot

*Updated Sat Oct 31 23:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42867 | 37378 | 5489 (62) | 4 | $-12097.43 | -4.5% |
| **+10¢** | 31966 | 25618 | 6348 (84) | 3 | $-10851.88 | -5.4% |
| **+15¢** | 26743 | 19900 | 6843 (112) | 4 | $-9925.29 | -5.9% |
| **+20¢** | 23751 | 16579 | 7172 (145) | 4 | $-8787.28 | -5.9% |
| **+10¢ (15¢ stop)** | 52292 | 52209 | 83 (48) | 1 | $-19813.05 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 23:11 | +10 stop | BTC | UP | 0.63 | open |  |
| 10-31 23:11 | +20 | BTC | UP | 0.63 | open |  |
| 10-31 23:11 | +15 | BTC | UP | 0.63 | open |  |
| 10-31 23:11 | +10 | BTC | UP | 0.63 | open |  |
| 10-31 23:11 | +5 | BTC | UP | 0.63 | open |  |
| 10-31 23:10 | +10 stop | XRP | UP | 0.67 | 0.79 | 0.92 |
| 10-31 23:10 | +20 | XRP | UP | 0.68 | open |  |
| 10-31 23:10 | +15 | XRP | UP | 0.68 | open |  |
| 10-31 23:10 | +10 | XRP | UP | 0.67 | 0.79 | 0.92 |
| 10-31 23:10 | +5 | XRP | UP | 0.66 | 0.73 | 0.40 |
| 10-31 23:08 | +10 stop | DOGE | DOWN | 0.42 | 0.53 | 0.74 |
| 10-31 23:08 | +10 | DOGE | DOWN | 0.43 | 0.53 | 0.64 |
| 10-31 23:08 | +5 | DOGE | DOWN | 0.43 | 0.53 | 0.64 |
| 10-31 23:07 | +10 stop | BTC | UP | 0.70 | 0.83 | 1.05 |
| 10-31 23:07 | +10 | BTC | UP | 0.70 | 0.83 | 1.05 |
| 10-31 23:07 | +5 | BTC | UP | 0.70 | 0.83 | 1.05 |
| 10-31 23:07 | +10 stop | DOGE | DOWN | 0.63 | 0.73 | 0.70 |
| 10-31 23:07 | +20 | DOGE | DOWN | 0.63 | 0.92 | 2.64 |
| 10-31 23:07 | +15 | DOGE | DOWN | 0.63 | 0.92 | 2.64 |
| 10-31 23:07 | +10 | DOGE | DOWN | 0.63 | 0.73 | 0.70 |
| 10-31 23:07 | +5 | DOGE | DOWN | 0.63 | 0.73 | 0.70 |
| 10-31 23:06 | +10 stop | NEAR | DOWN | 0.61 | 0.32 | -3.23 |
| 10-31 23:06 | +10 stop | BTC | UP | 0.57 | 0.68 | 0.76 |
| 10-31 23:06 | +20 | BTC | UP | 0.57 | 0.83 | 2.32 |
| 10-31 23:06 | +15 | BTC | UP | 0.57 | 0.73 | 1.28 |
| 10-31 23:06 | +10 | BTC | UP | 0.56 | 0.68 | 0.86 |
| 10-31 23:06 | +5 | BTC | UP | 0.56 | 0.68 | 0.86 |
| 10-31 23:05 | +10 stop | BNB | DOWN | 0.57 | 0.33 | -2.74 |
| 10-31 23:05 | +20 | BNB | DOWN | 0.57 | open |  |
| 10-31 23:05 | +15 | BNB | DOWN | 0.57 | open |  |
| 10-31 23:05 | +10 | BNB | DOWN | 0.57 | open |  |
| 10-31 23:05 | +5 | BNB | DOWN | 0.57 | open |  |
| 10-31 23:05 | +10 stop | XRP | DOWN | 0.56 | 0.34 | -2.54 |
| 10-31 23:04 | +10 stop | SOL | DOWN | 0.56 | 0.37 | -2.25 |
| 10-31 23:04 | +5 | SOL | DOWN | 0.56 | open |  |
| 10-31 23:03 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-31 23:03 | +10 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 10-31 23:03 | +10 stop | HYPE | UP | 0.56 | 0.78 | 1.85 |
| 10-31 23:03 | +10 stop | SOL | UP | 0.52 | 0.37 | -1.85 |
| 10-31 23:03 | +20 | SOL | UP | 0.52 | 0.76 | 2.09 |
