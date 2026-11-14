# Range-Scalp Bot

*Updated Sat Nov 14 11:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59368 | 51808 | 7560 (107) | 6 | $-15982.36 | -4.3% |
| **+10¢** | 44341 | 35491 | 8850 (142) | 6 | $-15000.90 | -5.4% |
| **+15¢** | 37158 | 27614 | 9544 (178) | 7 | $-13633.39 | -5.8% |
| **+20¢** | 33101 | 23083 | 10018 (230) | 7 | $-12011.66 | -5.8% |
| **+10¢ (15¢ stop)** | 72223 | 72081 | 142 (82) | 1 | $-26557.34 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 11:08 | +10 stop | DOGE | UP | 0.53 | open |  |
| 11-14 11:08 | +15 | DOGE | UP | 0.53 | open |  |
| 11-14 11:08 | +10 | DOGE | UP | 0.53 | open |  |
| 11-14 11:08 | +5 | DOGE | UP | 0.53 | 0.58 | 0.14 |
| 11-14 11:08 | +10 stop | SOL | UP | 0.66 | 0.49 | -2.04 |
| 11-14 11:07 | +10 stop | DOGE | DOWN | 0.52 | 0.35 | -2.04 |
| 11-14 11:07 | +15 | DOGE | DOWN | 0.44 | 0.61 | 1.35 |
| 11-14 11:07 | +10 | DOGE | DOWN | 0.44 | 0.61 | 1.35 |
| 11-14 11:07 | +5 | DOGE | DOWN | 0.44 | 0.61 | 1.35 |
| 11-14 11:06 | +10 stop | SOL | DOWN | 0.61 | 0.46 | -1.86 |
| 11-14 11:06 | +10 stop | NEAR | DOWN | 0.64 | 0.43 | -2.45 |
| 11-14 11:05 | +10 stop | SOL | DOWN | 0.69 | 0.54 | -1.83 |
| 11-14 11:04 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-14 11:03 | +5 | HYPE | DOWN | 0.67 | 0.85 | 1.55 |
| 11-14 11:03 | +5 | NEAR | UP | 0.71 | open |  |
| 11-14 11:03 | +10 stop | BTC | UP | 0.59 | 0.37 | -2.54 |
| 11-14 11:03 | +20 | BTC | UP | 0.59 | open |  |
| 11-14 11:03 | +15 | BTC | UP | 0.59 | open |  |
| 11-14 11:03 | +10 | BTC | UP | 0.59 | open |  |
| 11-14 11:03 | +5 | BTC | UP | 0.59 | open |  |
| 11-14 11:02 | +10 stop | ETH | UP | 0.59 | 0.44 | -1.85 |
| 11-14 11:02 | +20 | ETH | UP | 0.59 | open |  |
| 11-14 11:02 | +15 | ETH | UP | 0.59 | open |  |
| 11-14 11:02 | +10 | ETH | UP | 0.59 | open |  |
| 11-14 11:02 | +5 | ETH | UP | 0.59 | open |  |
| 11-14 11:01 | +10 stop | BNB | UP | 0.57 | 0.41 | -1.95 |
| 11-14 11:01 | +20 | BNB | UP | 0.57 | open |  |
| 11-14 11:01 | +15 | BNB | UP | 0.57 | open |  |
| 11-14 11:01 | +10 | BNB | UP | 0.57 | open |  |
| 11-14 11:01 | +5 | BNB | UP | 0.57 | open |  |
| 11-14 11:01 | +10 stop | HYPE | DOWN | 0.54 | 0.65 | 0.76 |
| 11-14 11:01 | +20 | HYPE | DOWN | 0.54 | 0.85 | 2.83 |
| 11-14 11:01 | +15 | HYPE | DOWN | 0.54 | 0.85 | 2.83 |
| 11-14 11:01 | +10 | HYPE | DOWN | 0.54 | 0.65 | 0.76 |
| 11-14 11:01 | +5 | HYPE | DOWN | 0.55 | 0.63 | 0.45 |
| 11-14 11:01 | +10 stop | XRP | UP | 0.67 | 0.32 | -3.82 |
| 11-14 11:01 | +20 | XRP | UP | 0.67 | open |  |
| 11-14 11:01 | +15 | XRP | UP | 0.67 | open |  |
| 11-14 11:01 | +10 | XRP | UP | 0.67 | open |  |
| 11-14 11:01 | +5 | XRP | UP | 0.67 | open |  |
