# Range-Scalp Bot

*Updated Wed Nov 11 06:40 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55546 | 48442 | 7104 (94) | 1 | $-15176.70 | -4.3% |
| **+10¢** | 41499 | 33210 | 8289 (124) | 1 | $-14124.55 | -5.4% |
| **+15¢** | 34794 | 25856 | 8938 (158) | 4 | $-12888.03 | -5.9% |
| **+20¢** | 30985 | 21611 | 9374 (207) | 5 | $-11261.72 | -5.8% |
| **+10¢ (15¢ stop)** | 67644 | 67526 | 118 (73) | 1 | $-24898.35 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 06:40 | +10 stop | DOGE | UP | 0.59 | open |  |
| 11-11 06:40 | +20 | DOGE | UP | 0.59 | open |  |
| 11-11 06:40 | +15 | DOGE | UP | 0.59 | open |  |
| 11-11 06:40 | +10 | DOGE | UP | 0.59 | open |  |
| 11-11 06:40 | +5 | DOGE | UP | 0.59 | open |  |
| 11-11 06:35 | +10 stop | XRP | UP | 0.71 | 0.84 | 1.05 |
| 11-11 06:35 | +10 | XRP | UP | 0.71 | 0.84 | 1.05 |
| 11-11 06:35 | +5 | XRP | UP | 0.71 | 0.76 | 0.22 |
| 11-11 06:34 | +10 stop | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 11-11 06:34 | +20 | HYPE | UP | 0.65 | open |  |
| 11-11 06:34 | +15 | HYPE | UP | 0.64 | 0.80 | 1.31 |
| 11-11 06:34 | +10 | HYPE | UP | 0.64 | 0.74 | 0.69 |
| 11-11 06:34 | +5 | HYPE | UP | 0.64 | 0.72 | 0.48 |
| 11-11 06:34 | +10 stop | BTC | UP | 0.58 | 0.76 | 1.49 |
| 11-11 06:34 | +10 | BTC | UP | 0.58 | 0.76 | 1.49 |
| 11-11 06:34 | +5 | ZEC | DOWN | 0.62 | 0.74 | 0.89 |
| 11-11 06:34 | +5 | ETH | UP | 0.64 | 0.73 | 0.59 |
| 11-11 06:33 | +5 | ZEC | DOWN | 0.46 | 0.56 | 0.64 |
| 11-11 06:33 | +5 | BTC | UP | 0.69 | 0.76 | 0.42 |
| 11-11 06:33 | +5 | HYPE | UP | 0.65 | 0.79 | 1.12 |
| 11-11 06:33 | +10 stop | SOL | UP | 0.64 | 0.78 | 1.10 |
| 11-11 06:33 | +10 | SOL | UP | 0.64 | 0.78 | 1.10 |
| 11-11 06:33 | +10 stop | XRP | UP | 0.64 | 0.75 | 0.79 |
| 11-11 06:33 | +10 | XRP | UP | 0.64 | 0.75 | 0.79 |
| 11-11 06:33 | +5 | XRP | UP | 0.64 | 0.75 | 0.79 |
| 11-11 06:33 | +5 | SOL | UP | 0.65 | 0.78 | 1.01 |
| 11-11 06:32 | +5 | ZEC | DOWN | 0.59 | 0.64 | 0.16 |
| 11-11 06:32 | +10 stop | XRP | DOWN | 0.47 | 0.60 | 0.95 |
| 11-11 06:32 | +20 | XRP | DOWN | 0.47 | open |  |
| 11-11 06:32 | +15 | XRP | DOWN | 0.47 | open |  |
| 11-11 06:32 | +10 | XRP | DOWN | 0.46 | 0.60 | 1.05 |
| 11-11 06:32 | +5 | XRP | DOWN | 0.46 | 0.60 | 1.05 |
| 11-11 06:32 | +10 stop | SOL | UP | 0.50 | 0.64 | 1.05 |
| 11-11 06:32 | +20 | SOL | UP | 0.50 | 0.78 | 2.49 |
| 11-11 06:32 | +15 | SOL | UP | 0.50 | 0.69 | 1.57 |
| 11-11 06:32 | +10 | SOL | UP | 0.50 | 0.64 | 1.05 |
| 11-11 06:32 | +5 | SOL | UP | 0.50 | 0.57 | 0.34 |
| 11-11 06:32 | +10 stop | HYPE | UP | 0.57 | 0.79 | 1.86 |
| 11-11 06:32 | +20 | HYPE | UP | 0.57 | 0.79 | 1.86 |
| 11-11 06:32 | +15 | HYPE | UP | 0.57 | 0.79 | 1.86 |
