# Range-Scalp Bot

*Updated Wed Oct 28 11:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38013 | 33171 | 4842 (46) | 7 | $-10684.45 | -4.5% |
| **+10¢** | 28356 | 22752 | 5604 (68) | 7 | $-9558.78 | -5.4% |
| **+15¢** | 23721 | 17705 | 6016 (93) | 7 | $-8507.89 | -5.7% |
| **+20¢** | 21038 | 14738 | 6300 (118) | 8 | $-7480.10 | -5.7% |
| **+10¢ (15¢ stop)** | 46543 | 46476 | 67 (35) | 3 | $-17746.40 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 11:23 | +10 stop | DOGE | UP | 0.59 | open |  |
| 10-28 11:23 | +10 stop | HYPE | UP | 0.48 | open |  |
| 10-28 11:22 | +10 stop | SOL | UP | 0.67 | open |  |
| 10-28 11:22 | +10 | SOL | UP | 0.67 | open |  |
| 10-28 11:22 | +5 | ZEC | DOWN | 0.71 | open |  |
| 10-28 11:21 | +10 stop | ETH | DOWN | 0.60 | 0.31 | -3.22 |
| 10-28 11:21 | +10 stop | HYPE | DOWN | 0.64 | 0.42 | -2.55 |
| 10-28 11:20 | +10 stop | DOGE | DOWN | 0.59 | 0.41 | -2.14 |
| 10-28 11:20 | +10 stop | XRP | DOWN | 0.71 | 0.47 | -2.73 |
| 10-28 11:19 | +10 stop | ETH | UP | 0.60 | 0.38 | -2.54 |
| 10-28 11:19 | +10 stop | NEAR | UP | 0.56 | 0.34 | -2.54 |
| 10-28 11:19 | +10 stop | XRP | UP | 0.54 | 0.36 | -2.15 |
| 10-28 11:19 | +10 stop | SOL | UP | 0.46 | 0.57 | 0.74 |
| 10-28 11:19 | +10 | SOL | UP | 0.46 | 0.57 | 0.74 |
| 10-28 11:19 | +5 | HYPE | UP | 0.69 | open |  |
| 10-28 11:19 | +5 | ZEC | DOWN | 0.61 | 0.69 | 0.48 |
| 10-28 11:19 | +10 stop | DOGE | UP | 0.62 | 0.38 | -2.74 |
| 10-28 11:19 | +20 | DOGE | UP | 0.62 | open |  |
| 10-28 11:19 | +15 | DOGE | UP | 0.62 | open |  |
| 10-28 11:19 | +10 | DOGE | UP | 0.62 | open |  |
| 10-28 11:19 | +5 | DOGE | UP | 0.62 | open |  |
| 10-28 11:18 | +10 stop | BNB | DOWN | 0.65 | 0.48 | -2.04 |
| 10-28 11:18 | +10 | BNB | DOWN | 0.65 | open |  |
| 10-28 11:18 | +5 | BNB | DOWN | 0.65 | open |  |
| 10-28 11:18 | +5 | SOL | DOWN | 0.67 | open |  |
| 10-28 11:18 | +5 | BTC | DOWN | 0.60 | open |  |
| 10-28 11:18 | +10 stop | ETH | DOWN | 0.52 | 0.35 | -2.04 |
| 10-28 11:18 | +10 stop | XRP | DOWN | 0.60 | 0.45 | -1.85 |
| 10-28 11:18 | +20 | XRP | DOWN | 0.60 | open |  |
| 10-28 11:18 | +15 | XRP | DOWN | 0.60 | 0.78 | 1.50 |
| 10-28 11:18 | +10 | XRP | DOWN | 0.60 | 0.71 | 0.78 |
| 10-28 11:18 | +5 | XRP | DOWN | 0.60 | 0.68 | 0.47 |
| 10-28 11:17 | +10 stop | SOL | DOWN | 0.57 | 0.67 | 0.66 |
| 10-28 11:17 | +20 | SOL | DOWN | 0.57 | open |  |
| 10-28 11:17 | +15 | SOL | DOWN | 0.57 | open |  |
| 10-28 11:17 | +10 | SOL | DOWN | 0.57 | 0.67 | 0.66 |
| 10-28 11:17 | +5 | SOL | DOWN | 0.57 | 0.64 | 0.35 |
| 10-28 11:16 | +10 stop | HYPE | UP | 0.57 | 0.39 | -2.15 |
| 10-28 11:16 | +20 | HYPE | UP | 0.57 | open |  |
| 10-28 11:16 | +15 | HYPE | UP | 0.57 | open |  |
