# Range-Scalp Bot

*Updated Fri Oct 23 23:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 31082 | 27086 | 3996 (40) | 4 | $-8982.72 | -4.6% |
| **+10¢** | 23247 | 18631 | 4616 (58) | 5 | $-7982.66 | -5.5% |
| **+15¢** | 19449 | 14483 | 4966 (81) | 6 | $-7184.66 | -5.9% |
| **+20¢** | 17226 | 12025 | 5201 (103) | 6 | $-6433.01 | -5.9% |
| **+10¢ (15¢ stop)** | 38143 | 38084 | 59 (32) | 0 | $-14611.33 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 23:09 | +10 stop | ETH | DOWN | 0.60 | 0.77 | 1.40 |
| 10-23 23:08 | +5 | NEAR | UP | 0.65 | open |  |
| 10-23 23:08 | +10 stop | ETH | DOWN | 0.71 | 0.56 | -1.83 |
| 10-23 23:08 | +20 | ETH | DOWN | 0.71 | 0.91 | 1.81 |
| 10-23 23:08 | +15 | ETH | DOWN | 0.71 | 0.91 | 1.81 |
| 10-23 23:08 | +10 | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 10-23 23:08 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
| 10-23 23:07 | +10 stop | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 10-23 23:07 | +10 stop | HYPE | DOWN | 0.52 | 0.68 | 1.26 |
| 10-23 23:07 | +10 stop | XRP | DOWN | 0.59 | 0.72 | 0.98 |
| 10-23 23:07 | +5 | XRP | DOWN | 0.59 | 0.66 | 0.37 |
| 10-23 23:07 | +10 stop | HYPE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-23 23:07 | +10 stop | NEAR | UP | 0.61 | 0.43 | -2.15 |
| 10-23 23:07 | +20 | NEAR | UP | 0.61 | open |  |
| 10-23 23:07 | +15 | NEAR | UP | 0.61 | open |  |
| 10-23 23:07 | +10 | NEAR | UP | 0.61 | open |  |
| 10-23 23:07 | +5 | NEAR | UP | 0.62 | 0.69 | 0.38 |
| 10-23 23:07 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-23 23:07 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-23 23:07 | +5 | BTC | DOWN | 0.64 | 0.72 | 0.48 |
| 10-23 23:06 | +10 stop | BTC | UP | 0.44 | 0.55 | 0.74 |
| 10-23 23:06 | +15 | BTC | UP | 0.45 | open |  |
| 10-23 23:06 | +10 | BTC | UP | 0.45 | 0.55 | 0.64 |
| 10-23 23:06 | +5 | BTC | UP | 0.45 | 0.55 | 0.64 |
| 10-23 23:06 | +10 stop | ZEC | UP | 0.54 | 0.26 | -3.12 |
| 10-23 23:06 | +20 | ZEC | UP | 0.54 | open |  |
| 10-23 23:06 | +15 | ZEC | UP | 0.54 | open |  |
| 10-23 23:06 | +10 | ZEC | UP | 0.54 | open |  |
| 10-23 23:06 | +5 | ZEC | UP | 0.54 | open |  |
| 10-23 23:06 | +10 stop | XRP | UP | 0.54 | 0.25 | -3.22 |
| 10-23 23:06 | +20 | XRP | UP | 0.54 | open |  |
| 10-23 23:06 | +15 | XRP | UP | 0.54 | open |  |
| 10-23 23:06 | +10 | XRP | UP | 0.54 | open |  |
| 10-23 23:06 | +5 | XRP | UP | 0.54 | 0.63 | 0.55 |
| 10-23 23:05 | +10 stop | SOL | UP | 0.60 | 0.42 | -2.15 |
| 10-23 23:05 | +15 | SOL | UP | 0.60 | open |  |
| 10-23 23:05 | +10 | SOL | UP | 0.60 | open |  |
| 10-23 23:05 | +5 | SOL | UP | 0.63 | open |  |
| 10-23 23:02 | +10 stop | SOL | UP | 0.71 | 0.56 | -1.83 |
| 10-23 23:02 | +20 | SOL | UP | 0.71 | open |  |
