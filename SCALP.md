# Range-Scalp Bot

*Updated Tue Oct 13 04:07 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14311 | 12374 | 1937 (27) | 4 | $-4634.50 | -5.1% |
| **+10¢** | 10824 | 8574 | 2250 (39) | 6 | $-4365.25 | -6.4% |
| **+15¢** | 9094 | 6689 | 2405 (57) | 6 | $-3876.39 | -6.8% |
| **+20¢** | 8093 | 5587 | 2506 (72) | 7 | $-3337.22 | -6.6% |
| **+10¢ (15¢ stop)** | 17534 | 17485 | 49 (29) | 5 | $-6768.44 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 04:07 | +10 stop | XRP | DOWN | 0.58 | open |  |
| 10-13 04:06 | +10 stop | BNB | DOWN | 0.64 | open |  |
| 10-13 04:06 | +15 | BNB | DOWN | 0.64 | open |  |
| 10-13 04:06 | +10 | BNB | DOWN | 0.64 | open |  |
| 10-13 04:06 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.18 |
| 10-13 04:05 | +5 | BTC | UP | 0.56 | open |  |
| 10-13 04:05 | +10 stop | DOGE | UP | 0.69 | open |  |
| 10-13 04:05 | +20 | DOGE | UP | 0.69 | open |  |
| 10-13 04:05 | +15 | DOGE | UP | 0.69 | open |  |
| 10-13 04:05 | +10 | DOGE | UP | 0.69 | open |  |
| 10-13 04:05 | +5 | DOGE | UP | 0.69 | open |  |
| 10-13 04:05 | +10 stop | ZEC | UP | 0.57 | open |  |
| 10-13 04:05 | +10 stop | ETH | UP | 0.54 | open |  |
| 10-13 04:05 | +15 | ETH | UP | 0.54 | open |  |
| 10-13 04:05 | +10 | ETH | UP | 0.54 | open |  |
| 10-13 04:05 | +5 | ETH | UP | 0.54 | 0.62 | 0.45 |
| 10-13 04:05 | +5 | XRP | UP | 0.57 | open |  |
| 10-13 04:05 | +10 | XRP | UP | 0.60 | open |  |
| 10-13 04:05 | +5 | XRP | UP | 0.60 | 0.69 | 0.58 |
| 10-13 04:03 | +5 | ETH | UP | 0.66 | 0.71 | 0.19 |
| 10-13 04:02 | +5 | DOGE | UP | 0.69 | 0.80 | 0.83 |
| 10-13 04:01 | +10 stop | ZEC | UP | 0.71 | 0.83 | 0.98 |
| 10-13 04:01 | +10 stop | HYPE | UP | 0.59 | 0.71 | 0.84 |
| 10-13 04:01 | +20 | HYPE | UP | 0.59 | 0.80 | 1.77 |
| 10-13 04:01 | +15 | HYPE | UP | 0.58 | 0.74 | 1.28 |
| 10-13 04:01 | +10 | HYPE | UP | 0.60 | 0.71 | 0.78 |
| 10-13 04:01 | +5 | HYPE | UP | 0.60 | 0.66 | 0.27 |
| 10-13 04:01 | +10 stop | ETH | UP | 0.58 | 0.69 | 0.77 |
| 10-13 04:01 | +20 | ETH | UP | 0.58 | open |  |
| 10-13 04:01 | +15 | ETH | UP | 0.58 | 0.74 | 1.28 |
| 10-13 04:01 | +10 | ETH | UP | 0.58 | 0.69 | 0.77 |
| 10-13 04:01 | +5 | ETH | UP | 0.58 | 0.64 | 0.25 |
| 10-13 04:01 | +10 stop | BTC | UP | 0.68 | 0.52 | -1.94 |
| 10-13 04:01 | +20 | BTC | UP | 0.68 | open |  |
| 10-13 04:01 | +15 | BTC | UP | 0.68 | open |  |
| 10-13 04:01 | +10 | BTC | UP | 0.68 | open |  |
| 10-13 04:01 | +5 | BTC | UP | 0.68 | 0.77 | 0.61 |
| 10-13 04:01 | +10 stop | SOL | UP | 0.68 | 0.79 | 0.80 |
| 10-13 04:01 | +20 | SOL | UP | 0.68 | open |  |
| 10-13 04:01 | +15 | SOL | UP | 0.68 | 0.83 | 1.25 |
