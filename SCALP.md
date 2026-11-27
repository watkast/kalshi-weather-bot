# Range-Scalp Bot

*Updated Fri Nov 27 06:23 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 73448 | 64099 | 9349 (165) | 1 | $-19572.32 | -4.2% |
| **+10¢** | 54733 | 43817 | 10916 (210) | 1 | $-18193.17 | -5.3% |
| **+15¢** | 45836 | 34078 | 11758 (268) | 2 | $-16291.69 | -5.7% |
| **+20¢** | 40793 | 28412 | 12381 (334) | 1 | $-14692.70 | -5.7% |
| **+10¢ (15¢ stop)** | 89459 | 89247 | 212 (129) | 1 | $-33094.51 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-27 06:23 | +10 stop | HYPE | UP | 0.71 | open |  |
| 11-27 06:23 | +15 | HYPE | UP | 0.71 | open |  |
| 11-27 06:23 | +10 | HYPE | UP | 0.70 | open |  |
| 11-27 06:23 | +5 | HYPE | UP | 0.70 | open |  |
| 11-27 06:21 | +10 stop | NEAR | DOWN | 0.56 | 0.70 | 1.07 |
| 11-27 06:21 | +20 | NEAR | DOWN | 0.57 | 0.77 | 1.69 |
| 11-27 06:21 | +15 | NEAR | DOWN | 0.64 | open |  |
| 11-27 06:21 | +10 | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 11-27 06:21 | +5 | NEAR | DOWN | 0.64 | 0.70 | 0.28 |
| 11-27 06:21 | +5 | XRP | DOWN | 0.57 | 0.69 | 0.87 |
| 11-27 06:21 | +10 stop | XRP | DOWN | 0.63 | 0.84 | 1.83 |
| 11-27 06:20 | +10 stop | BNB | DOWN | 0.64 | 0.86 | 1.94 |
| 11-27 06:20 | +10 stop | BTC | DOWN | 0.57 | 0.89 | 2.95 |
| 11-27 06:20 | +10 stop | NEAR | UP | 0.54 | 0.22 | -3.51 |
| 11-27 06:20 | +10 stop | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 11-27 06:19 | +10 stop | DOGE | UP | 0.52 | 0.17 | -3.78 |
| 11-27 06:19 | +10 stop | XRP | UP | 0.58 | 0.42 | -2.00 |
| 11-27 06:18 | +10 stop | ZEC | DOWN | 0.66 | 0.80 | 1.12 |
| 11-27 06:18 | +5 | ZEC | DOWN | 0.66 | 0.74 | 0.50 |
| 11-27 06:18 | +15 | ETH | DOWN | 0.68 | 0.87 | 1.66 |
| 11-27 06:18 | +10 | ETH | DOWN | 0.68 | 0.87 | 1.66 |
| 11-27 06:18 | +5 | ETH | DOWN | 0.68 | 0.77 | 0.61 |
| 11-27 06:18 | +10 stop | HYPE | UP | 0.61 | 0.71 | 0.72 |
| 11-27 06:18 | +20 | HYPE | UP | 0.62 | open |  |
| 11-27 06:18 | +15 | HYPE | UP | 0.59 | 0.75 | 1.33 |
| 11-27 06:18 | +10 | HYPE | UP | 0.59 | 0.71 | 0.88 |
| 11-27 06:18 | +5 | HYPE | UP | 0.60 | 0.71 | 0.78 |
| 11-27 06:17 | +10 stop | ZEC | DOWN | 0.52 | 0.70 | 1.47 |
| 11-27 06:17 | +10 stop | DOGE | DOWN | 0.58 | 0.37 | -2.45 |
| 11-27 06:17 | +20 | DOGE | DOWN | 0.58 | 0.82 | 2.11 |
| 11-27 06:17 | +15 | DOGE | DOWN | 0.58 | 0.82 | 2.11 |
| 11-27 06:17 | +10 | DOGE | DOWN | 0.58 | 0.82 | 2.11 |
| 11-27 06:17 | +5 | DOGE | DOWN | 0.58 | 0.82 | 2.11 |
| 11-27 06:17 | +10 stop | XRP | DOWN | 0.62 | 0.35 | -2.99 |
| 11-27 06:17 | +10 stop | SOL | DOWN | 0.66 | 0.42 | -2.74 |
| 11-27 06:17 | +20 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 11-27 06:17 | +15 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 11-27 06:17 | +10 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 11-27 06:17 | +5 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 11-27 06:17 | +10 stop | ETH | DOWN | 0.71 | 0.56 | -1.83 |
