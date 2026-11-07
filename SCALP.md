# Range-Scalp Bot

*Updated Sat Nov 07 00:19 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50191 | 43753 | 6438 (76) | 3 | $-14101.21 | -4.5% |
| **+10¢** | 37452 | 29958 | 7494 (102) | 4 | $-13017.11 | -5.5% |
| **+15¢** | 31368 | 23291 | 8077 (131) | 5 | $-11935.76 | -6.1% |
| **+20¢** | 27887 | 19419 | 8468 (173) | 6 | $-10551.64 | -6.0% |
| **+10¢ (15¢ stop)** | 61110 | 61011 | 99 (58) | 4 | $-22638.44 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 00:19 | +5 | XRP | DOWN | 0.54 | 0.65 | 0.76 |
| 11-07 00:19 | +10 stop | ETH | UP | 0.71 | open |  |
| 11-07 00:19 | +20 | ETH | UP | 0.71 | open |  |
| 11-07 00:19 | +15 | ETH | UP | 0.70 | open |  |
| 11-07 00:19 | +10 | ETH | UP | 0.70 | open |  |
| 11-07 00:19 | +5 | ETH | UP | 0.70 | open |  |
| 11-07 00:17 | +10 stop | DOGE | UP | 0.70 | 0.84 | 1.15 |
| 11-07 00:17 | +10 | DOGE | UP | 0.70 | 0.84 | 1.15 |
| 11-07 00:17 | +5 | DOGE | UP | 0.70 | 0.75 | 0.21 |
| 11-07 00:17 | +10 stop | ZEC | DOWN | 0.58 | open |  |
| 11-07 00:17 | +20 | ZEC | DOWN | 0.58 | open |  |
| 11-07 00:17 | +15 | ZEC | DOWN | 0.58 | open |  |
| 11-07 00:17 | +10 | ZEC | DOWN | 0.58 | open |  |
| 11-07 00:17 | +5 | ZEC | DOWN | 0.58 | open |  |
| 11-07 00:16 | +10 stop | HYPE | UP | 0.55 | 0.69 | 1.07 |
| 11-07 00:16 | +20 | HYPE | UP | 0.55 | 0.76 | 1.79 |
| 11-07 00:16 | +15 | HYPE | UP | 0.55 | 0.73 | 1.48 |
| 11-07 00:16 | +10 | HYPE | UP | 0.55 | 0.69 | 1.07 |
| 11-07 00:16 | +5 | HYPE | UP | 0.55 | 0.64 | 0.55 |
| 11-07 00:16 | +10 stop | BNB | UP | 0.66 | 0.76 | 0.71 |
| 11-07 00:16 | +20 | BNB | UP | 0.66 | open |  |
| 11-07 00:16 | +15 | BNB | UP | 0.66 | open |  |
| 11-07 00:16 | +10 | BNB | UP | 0.66 | 0.76 | 0.71 |
| 11-07 00:16 | +5 | BNB | UP | 0.66 | 0.72 | 0.29 |
| 11-07 00:16 | +10 stop | SOL | UP | 0.60 | 0.77 | 1.40 |
| 11-07 00:16 | +20 | SOL | UP | 0.60 | open |  |
| 11-07 00:16 | +15 | SOL | UP | 0.60 | 0.77 | 1.40 |
| 11-07 00:16 | +10 | SOL | UP | 0.60 | 0.77 | 1.40 |
| 11-07 00:16 | +5 | SOL | UP | 0.60 | 0.65 | 0.17 |
| 11-07 00:16 | +10 stop | DOGE | UP | 0.56 | 0.67 | 0.76 |
| 11-07 00:16 | +20 | DOGE | UP | 0.56 | 0.84 | 2.52 |
| 11-07 00:16 | +15 | DOGE | UP | 0.56 | 0.71 | 1.17 |
| 11-07 00:16 | +10 | DOGE | UP | 0.56 | 0.67 | 0.76 |
| 11-07 00:16 | +5 | DOGE | UP | 0.56 | 0.67 | 0.76 |
| 11-07 00:16 | +10 stop | XRP | DOWN | 0.71 | open |  |
| 11-07 00:16 | +20 | XRP | DOWN | 0.71 | open |  |
| 11-07 00:16 | +15 | XRP | DOWN | 0.71 | open |  |
| 11-07 00:16 | +10 | XRP | DOWN | 0.71 | open |  |
| 11-07 00:16 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 11-07 00:16 | +10 stop | NEAR | UP | 0.61 | open |  |
