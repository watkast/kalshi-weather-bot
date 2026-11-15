# Range-Scalp Bot

*Updated Sun Nov 15 21:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61235 | 53434 | 7801 (114) | 3 | $-16484.71 | -4.3% |
| **+10¢** | 45727 | 36588 | 9139 (153) | 5 | $-15474.64 | -5.4% |
| **+15¢** | 38301 | 28446 | 9855 (191) | 6 | $-14109.42 | -5.9% |
| **+20¢** | 34139 | 23801 | 10338 (243) | 6 | $-12378.97 | -5.8% |
| **+10¢ (15¢ stop)** | 74514 | 74362 | 152 (90) | 0 | $-27433.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 21:11 | +10 stop | NEAR | UP | 0.49 | 0.14 | -3.77 |
| 11-15 21:08 | +10 stop | SOL | UP | 0.68 | 0.50 | -2.14 |
| 11-15 21:08 | +10 | SOL | UP | 0.68 | 0.81 | 1.03 |
| 11-15 21:08 | +5 | SOL | UP | 0.68 | 0.76 | 0.51 |
| 11-15 21:08 | +10 stop | NEAR | UP | 0.55 | 0.40 | -1.85 |
| 11-15 21:08 | +20 | NEAR | UP | 0.55 | open |  |
| 11-15 21:08 | +15 | NEAR | UP | 0.55 | open |  |
| 11-15 21:08 | +10 | NEAR | UP | 0.55 | open |  |
| 11-15 21:08 | +5 | NEAR | UP | 0.55 | open |  |
| 11-15 21:08 | +10 stop | HYPE | DOWN | 0.55 | 0.36 | -2.25 |
| 11-15 21:07 | +10 stop | ZEC | DOWN | 0.60 | 0.71 | 0.78 |
| 11-15 21:07 | +5 | ZEC | DOWN | 0.60 | 0.69 | 0.58 |
| 11-15 21:06 | +5 | ETH | DOWN | 0.71 | 0.79 | 0.53 |
| 11-15 21:06 | +10 stop | SOL | UP | 0.53 | 0.29 | -2.73 |
| 11-15 21:06 | +5 | SOL | UP | 0.53 | 0.60 | 0.35 |
| 11-15 21:06 | +10 stop | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-15 21:05 | +5 | ETH | UP | 0.45 | 0.62 | 1.35 |
| 11-15 21:05 | +10 stop | ETH | UP | 0.49 | 0.62 | 0.95 |
| 11-15 21:05 | +5 | ETH | UP | 0.49 | 0.57 | 0.44 |
| 11-15 21:04 | +10 stop | ZEC | UP | 0.65 | 0.50 | -1.84 |
| 11-15 21:04 | +10 stop | NEAR | UP | 0.68 | 0.84 | 1.36 |
| 11-15 21:04 | +10 | NEAR | UP | 0.68 | 0.84 | 1.36 |
| 11-15 21:04 | +5 | NEAR | UP | 0.68 | 0.84 | 1.36 |
| 11-15 21:04 | +10 stop | XRP | UP | 0.59 | 0.79 | 1.71 |
| 11-15 21:04 | +10 stop | SOL | UP | 0.59 | 0.70 | 0.78 |
| 11-15 21:04 | +5 | SOL | UP | 0.59 | 0.70 | 0.78 |
| 11-15 21:04 | +5 | ETH | UP | 0.52 | 0.58 | 0.24 |
| 11-15 21:03 | +10 stop | HYPE | UP | 0.67 | 0.50 | -2.04 |
| 11-15 21:03 | +5 | XRP | UP | 0.65 | 0.79 | 1.12 |
| 11-15 21:03 | +5 | BTC | DOWN | 0.55 | 0.60 | 0.15 |
| 11-15 21:03 | +5 | ZEC | DOWN | 0.64 | 0.70 | 0.28 |
| 11-15 21:03 | +5 | DOGE | UP | 0.66 | 0.76 | 0.71 |
| 11-15 21:03 | +10 stop | NEAR | UP | 0.60 | 0.73 | 0.99 |
| 11-15 21:03 | +20 | NEAR | UP | 0.60 | 0.84 | 2.13 |
| 11-15 21:03 | +15 | NEAR | UP | 0.60 | 0.84 | 2.13 |
| 11-15 21:03 | +10 | NEAR | UP | 0.60 | 0.73 | 0.99 |
| 11-15 21:03 | +5 | NEAR | UP | 0.60 | 0.73 | 0.99 |
| 11-15 21:03 | +10 | XRP | DOWN | 0.48 | open |  |
| 11-15 21:03 | +5 | SOL | DOWN | 0.49 | 0.56 | 0.34 |
| 11-15 21:02 | +5 | XRP | DOWN | 0.59 | 0.66 | 0.37 |
