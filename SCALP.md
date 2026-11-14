# Range-Scalp Bot

*Updated Sat Nov 14 00:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58730 | 51241 | 7489 (106) | 2 | $-15875.91 | -4.3% |
| **+10¢** | 43872 | 35114 | 8758 (139) | 3 | $-14857.78 | -5.4% |
| **+15¢** | 36771 | 27337 | 9434 (174) | 4 | $-13436.25 | -5.8% |
| **+20¢** | 32760 | 22856 | 9904 (225) | 4 | $-11822.87 | -5.8% |
| **+10¢ (15¢ stop)** | 71507 | 71369 | 138 (82) | 2 | $-26342.33 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 00:05 | +10 stop | HYPE | DOWN | 0.47 | 0.59 | 0.85 |
| 11-14 00:05 | +10 stop | XRP | UP | 0.61 | open |  |
| 11-14 00:05 | +10 | XRP | UP | 0.61 | open |  |
| 11-14 00:05 | +5 | XRP | UP | 0.61 | 0.66 | 0.17 |
| 11-14 00:04 | +10 stop | SOL | UP | 0.64 | open |  |
| 11-14 00:04 | +20 | SOL | UP | 0.64 | open |  |
| 11-14 00:04 | +15 | SOL | UP | 0.64 | open |  |
| 11-14 00:04 | +10 | SOL | UP | 0.64 | open |  |
| 11-14 00:04 | +5 | SOL | UP | 0.64 | open |  |
| 11-14 00:04 | +10 stop | HYPE | UP | 0.53 | 0.38 | -1.85 |
| 11-14 00:04 | +10 | HYPE | UP | 0.53 | open |  |
| 11-14 00:04 | +5 | HYPE | UP | 0.53 | open |  |
| 11-14 00:01 | +10 stop | BTC | UP | 0.69 | 0.80 | 0.83 |
| 11-14 00:01 | +20 | BTC | UP | 0.69 | open |  |
| 11-14 00:01 | +15 | BTC | UP | 0.69 | open |  |
| 11-14 00:01 | +10 | BTC | UP | 0.69 | 0.80 | 0.83 |
| 11-14 00:01 | +5 | BTC | UP | 0.69 | 0.74 | 0.21 |
| 11-14 00:01 | +10 stop | XRP | UP | 0.68 | 0.79 | 0.82 |
| 11-14 00:01 | +20 | XRP | UP | 0.68 | open |  |
| 11-14 00:01 | +15 | XRP | UP | 0.68 | open |  |
| 11-14 00:01 | +10 | XRP | UP | 0.68 | 0.79 | 0.82 |
| 11-14 00:01 | +5 | XRP | UP | 0.68 | 0.76 | 0.51 |
| 11-14 00:01 | +10 stop | HYPE | UP | 0.66 | 0.77 | 0.81 |
| 11-14 00:01 | +20 | HYPE | UP | 0.66 | open |  |
| 11-14 00:01 | +15 | HYPE | UP | 0.66 | open |  |
| 11-14 00:01 | +10 | HYPE | UP | 0.66 | 0.77 | 0.81 |
| 11-14 00:01 | +5 | HYPE | UP | 0.66 | 0.72 | 0.29 |
| 11-13 22:17 | +10 stop | DOGE | DOWN | 0.56 | yes | -5.78 |
| 11-13 22:17 | +20 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 11-13 22:17 | +15 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 11-13 22:17 | +10 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 11-13 22:17 | +5 | DOGE | DOWN | 0.56 | yes | -5.78 |
| 11-13 22:17 | +5 | SOL | UP | 0.69 | yes | 2.95 |
| 11-13 22:16 | +10 stop | ETH | DOWN | 0.59 | yes | -6.07 |
| 11-13 22:16 | +20 | ETH | DOWN | 0.59 | yes | -6.07 |
| 11-13 22:16 | +15 | ETH | DOWN | 0.60 | yes | -6.17 |
| 11-13 22:16 | +10 | ETH | DOWN | 0.60 | yes | -6.17 |
| 11-13 22:16 | +5 | ETH | DOWN | 0.60 | yes | -6.17 |
| 11-13 22:16 | +10 stop | BTC | DOWN | 0.56 | yes | -5.78 |
| 11-13 22:16 | +20 | BTC | DOWN | 0.55 | yes | -5.68 |
