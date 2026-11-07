# Range-Scalp Bot

*Updated Sat Nov 07 23:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 51675 | 45056 | 6619 (80) | 3 | $-14342.65 | -4.4% |
| **+10¢** | 38560 | 30842 | 7718 (106) | 4 | $-13359.54 | -5.5% |
| **+15¢** | 32287 | 23969 | 8318 (135) | 4 | $-12264.36 | -6.1% |
| **+20¢** | 28719 | 19998 | 8721 (180) | 6 | $-10820.70 | -6.0% |
| **+10¢ (15¢ stop)** | 62920 | 62817 | 103 (61) | 3 | $-23309.07 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 23:33 | +10 stop | SOL | UP | 0.53 | open |  |
| 11-07 23:33 | +10 | SOL | UP | 0.54 | open |  |
| 11-07 23:33 | +5 | SOL | UP | 0.55 | open |  |
| 11-07 23:33 | +10 stop | XRP | UP | 0.60 | open |  |
| 11-07 23:33 | +10 | XRP | UP | 0.60 | open |  |
| 11-07 23:33 | +5 | XRP | UP | 0.60 | open |  |
| 11-07 23:32 | +5 | DOGE | UP | 0.61 | 0.72 | 0.78 |
| 11-07 23:32 | +5 | XRP | UP | 0.60 | 0.65 | 0.17 |
| 11-07 23:32 | +10 stop | HYPE | UP | 0.60 | 0.70 | 0.68 |
| 11-07 23:32 | +20 | HYPE | UP | 0.61 | open |  |
| 11-07 23:32 | +15 | HYPE | UP | 0.61 | open |  |
| 11-07 23:32 | +10 | HYPE | UP | 0.61 | open |  |
| 11-07 23:32 | +5 | HYPE | UP | 0.61 | 0.67 | 0.27 |
| 11-07 23:32 | +10 stop | SOL | UP | 0.63 | 0.74 | 0.79 |
| 11-07 23:32 | +20 | SOL | UP | 0.63 | open |  |
| 11-07 23:32 | +15 | SOL | UP | 0.63 | open |  |
| 11-07 23:32 | +10 | SOL | UP | 0.63 | 0.74 | 0.79 |
| 11-07 23:32 | +5 | SOL | UP | 0.63 | 0.74 | 0.79 |
| 11-07 23:31 | +10 stop | DOGE | UP | 0.58 | 0.72 | 1.07 |
| 11-07 23:31 | +20 | DOGE | UP | 0.58 | 0.79 | 1.80 |
| 11-07 23:31 | +15 | DOGE | UP | 0.58 | 0.75 | 1.38 |
| 11-07 23:31 | +10 | DOGE | UP | 0.58 | 0.72 | 1.07 |
| 11-07 23:31 | +5 | DOGE | UP | 0.58 | 0.64 | 0.25 |
| 11-07 23:31 | +10 stop | XRP | UP | 0.55 | 0.65 | 0.71 |
| 11-07 23:31 | +20 | XRP | UP | 0.54 | open |  |
| 11-07 23:31 | +15 | XRP | UP | 0.54 | open |  |
| 11-07 23:31 | +10 | XRP | UP | 0.54 | 0.65 | 0.74 |
| 11-07 23:31 | +5 | XRP | UP | 0.54 | 0.60 | 0.23 |
| 11-07 23:31 | +10 stop | BTC | UP | 0.60 | 0.70 | 0.68 |
| 11-07 23:31 | +20 | BTC | UP | 0.60 | open |  |
| 11-07 23:31 | +15 | BTC | UP | 0.60 | 0.75 | 1.19 |
| 11-07 23:31 | +10 | BTC | UP | 0.60 | 0.70 | 0.68 |
| 11-07 23:31 | +5 | BTC | UP | 0.60 | 0.70 | 0.68 |
| 11-07 23:31 | +10 stop | ETH | UP | 0.62 | 0.72 | 0.68 |
| 11-07 23:31 | +10 | ETH | UP | 0.62 | 0.72 | 0.68 |
| 11-07 23:31 | +5 | ETH | UP | 0.62 | 0.72 | 0.68 |
| 11-07 23:31 | +10 stop | ZEC | DOWN | 0.62 | open |  |
| 11-07 23:31 | +20 | ZEC | DOWN | 0.62 | open |  |
| 11-07 23:31 | +15 | ZEC | DOWN | 0.62 | open |  |
| 11-07 23:31 | +10 | ZEC | DOWN | 0.62 | open |  |
