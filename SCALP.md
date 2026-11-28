# Range-Scalp Bot

*Updated Sat Nov 28 01:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74177 | 64748 | 9429 (171) | 3 | $-19657.65 | -4.2% |
| **+10¢** | 55266 | 44251 | 11015 (217) | 3 | $-18275.11 | -5.3% |
| **+15¢** | 46279 | 34416 | 11863 (275) | 4 | $-16327.68 | -5.6% |
| **+20¢** | 41183 | 28688 | 12495 (342) | 5 | $-14740.54 | -5.7% |
| **+10¢ (15¢ stop)** | 90280 | 90061 | 219 (135) | 3 | $-33331.78 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 01:33 | +10 stop | XRP | UP | 0.71 | open |  |
| 11-28 01:33 | +10 | XRP | UP | 0.71 | open |  |
| 11-28 01:33 | +5 | XRP | UP | 0.71 | open |  |
| 11-28 01:32 | +5 | NEAR | UP | 0.67 | open |  |
| 11-28 01:32 | +5 | ZEC | UP | 0.66 | 0.71 | 0.19 |
| 11-28 01:31 | +10 stop | HYPE | UP | 0.71 | open |  |
| 11-28 01:31 | +20 | HYPE | UP | 0.71 | open |  |
| 11-28 01:31 | +15 | HYPE | UP | 0.71 | open |  |
| 11-28 01:31 | +10 | HYPE | UP | 0.70 | open |  |
| 11-28 01:31 | +5 | HYPE | UP | 0.70 | open |  |
| 11-28 01:31 | +10 stop | NEAR | UP | 0.66 | open |  |
| 11-28 01:31 | +20 | NEAR | UP | 0.66 | open |  |
| 11-28 01:31 | +15 | NEAR | UP | 0.66 | open |  |
| 11-28 01:31 | +10 | NEAR | UP | 0.66 | open |  |
| 11-28 01:31 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 11-28 01:30 | +10 stop | ZEC | UP | 0.61 | 0.71 | 0.68 |
| 11-28 01:30 | +20 | ZEC | UP | 0.61 | open |  |
| 11-28 01:30 | +15 | ZEC | UP | 0.60 | open |  |
| 11-28 01:30 | +10 | ZEC | UP | 0.60 | 0.71 | 0.78 |
| 11-28 01:30 | +5 | ZEC | UP | 0.60 | 0.67 | 0.32 |
| 11-28 01:30 | +10 stop | SOL | UP | 0.56 | 0.70 | 1.07 |
| 11-28 01:30 | +20 | SOL | UP | 0.56 | open |  |
| 11-28 01:30 | +15 | SOL | UP | 0.56 | 0.72 | 1.27 |
| 11-28 01:30 | +10 | SOL | UP | 0.56 | 0.70 | 1.07 |
| 11-28 01:30 | +5 | SOL | UP | 0.56 | 0.64 | 0.45 |
| 11-28 01:30 | +10 stop | XRP | UP | 0.66 | 0.77 | 0.81 |
| 11-28 01:30 | +20 | XRP | UP | 0.66 | open |  |
| 11-28 01:30 | +15 | XRP | UP | 0.66 | open |  |
| 11-28 01:30 | +10 | XRP | UP | 0.66 | 0.77 | 0.81 |
| 11-28 01:30 | +5 | XRP | UP | 0.66 | 0.71 | 0.19 |
| 11-28 01:18 | +5 | XRP | UP | 0.70 | 0.77 | 0.42 |
| 11-28 01:16 | +10 stop | SOL | UP | 0.67 | 0.78 | 0.81 |
| 11-28 01:16 | +20 | SOL | UP | 0.67 | 0.87 | 1.76 |
| 11-28 01:16 | +15 | SOL | UP | 0.67 | 0.86 | 1.65 |
| 11-28 01:16 | +10 | SOL | UP | 0.67 | 0.78 | 0.81 |
| 11-28 01:16 | +5 | SOL | UP | 0.67 | 0.73 | 0.30 |
| 11-28 01:16 | +10 stop | DOGE | UP | 0.62 | 0.75 | 0.99 |
| 11-28 01:16 | +20 | DOGE | UP | 0.62 | 0.86 | 2.14 |
| 11-28 01:16 | +15 | DOGE | UP | 0.62 | 0.86 | 2.14 |
| 11-28 01:16 | +10 | DOGE | UP | 0.62 | 0.75 | 0.99 |
