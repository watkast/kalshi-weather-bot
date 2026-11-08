# Range-Scalp Bot

*Updated Sun Nov 08 08:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52198 | 45513 | 6685 (82) | 2 | $-14459.60 | -4.4% |
| **+10¢** | 38958 | 31164 | 7794 (107) | 3 | $-13464.78 | -5.5% |
| **+15¢** | 32631 | 24231 | 8400 (137) | 4 | $-12336.55 | -6.0% |
| **+20¢** | 29026 | 20221 | 8805 (181) | 4 | $-10861.52 | -6.0% |
| **+10¢ (15¢ stop)** | 63535 | 63430 | 105 (62) | 0 | $-23486.26 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 08:25 | +10 stop | NEAR | DOWN | 0.45 | 0.60 | 1.15 |
| 11-08 08:25 | +15 | NEAR | DOWN | 0.45 | 0.60 | 1.15 |
| 11-08 08:25 | +10 | NEAR | DOWN | 0.45 | 0.60 | 1.15 |
| 11-08 08:25 | +5 | NEAR | DOWN | 0.45 | 0.60 | 1.15 |
| 11-08 08:24 | +10 stop | SOL | UP | 0.69 | 0.80 | 0.83 |
| 11-08 08:24 | +15 | SOL | UP | 0.69 | open |  |
| 11-08 08:24 | +10 | SOL | UP | 0.69 | 0.80 | 0.83 |
| 11-08 08:24 | +5 | SOL | UP | 0.69 | 0.80 | 0.83 |
| 11-08 08:24 | +5 | SOL | DOWN | 0.44 | 0.60 | 1.25 |
| 11-08 08:22 | +10 stop | XRP | DOWN | 0.49 | 0.29 | -2.33 |
| 11-08 08:21 | +10 stop | SOL | DOWN | 0.71 | 0.32 | -4.21 |
| 11-08 08:21 | +5 | SOL | DOWN | 0.71 | 0.80 | 0.63 |
| 11-08 08:21 | +10 stop | XRP | DOWN | 0.48 | 0.63 | 1.15 |
| 11-08 08:19 | +10 stop | ZEC | DOWN | 0.69 | 0.84 | 1.25 |
| 11-08 08:18 | +5 | HYPE | DOWN | 0.68 | 0.73 | 0.20 |
| 11-08 08:18 | +5 | NEAR | DOWN | 0.63 | 0.73 | 0.69 |
| 11-08 08:17 | +10 stop | ZEC | DOWN | 0.68 | 0.50 | -2.14 |
| 11-08 08:17 | +10 stop | NEAR | DOWN | 0.70 | 0.80 | 0.73 |
| 11-08 08:17 | +5 | SOL | DOWN | 0.58 | 0.67 | 0.56 |
| 11-08 08:17 | +10 stop | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-08 08:17 | +20 | ETH | DOWN | 0.67 | 0.89 | 1.97 |
| 11-08 08:17 | +15 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-08 08:17 | +10 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-08 08:17 | +5 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-08 08:16 | +5 | BNB | UP | 0.57 | open |  |
| 11-08 08:16 | +10 stop | ZEC | UP | 0.59 | 0.42 | -2.05 |
| 11-08 08:16 | +20 | ZEC | UP | 0.59 | open |  |
| 11-08 08:16 | +15 | ZEC | UP | 0.59 | open |  |
| 11-08 08:16 | +10 | ZEC | UP | 0.59 | open |  |
| 11-08 08:16 | +5 | ZEC | UP | 0.59 | open |  |
| 11-08 08:16 | +10 stop | DOGE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-08 08:16 | +20 | DOGE | DOWN | 0.63 | 0.83 | 1.73 |
| 11-08 08:16 | +15 | DOGE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-08 08:16 | +10 | DOGE | DOWN | 0.63 | 0.79 | 1.31 |
| 11-08 08:16 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 11-08 08:15 | +10 stop | XRP | UP | 0.62 | 0.21 | -4.39 |
| 11-08 08:15 | +20 | XRP | UP | 0.62 | open |  |
| 11-08 08:15 | +15 | XRP | UP | 0.62 | open |  |
| 11-08 08:15 | +10 | XRP | UP | 0.62 | open |  |
| 11-08 08:15 | +5 | XRP | UP | 0.62 | 0.70 | 0.48 |
