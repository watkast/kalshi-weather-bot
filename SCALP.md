# Range-Scalp Bot

*Updated Tue Nov 17 04:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62535 | 54555 | 7980 (117) | 1 | $-16950.45 | -4.3% |
| **+10¢** | 46708 | 37372 | 9336 (159) | 2 | $-15810.83 | -5.4% |
| **+15¢** | 39151 | 29081 | 10070 (201) | 2 | $-14357.86 | -5.8% |
| **+20¢** | 34897 | 24337 | 10560 (256) | 2 | $-12523.35 | -5.7% |
| **+10¢ (15¢ stop)** | 76116 | 75960 | 156 (92) | 0 | $-28032.32 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 04:03 | +10 stop | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-17 04:03 | +10 | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-17 04:03 | +5 | ZEC | DOWN | 0.69 | 0.76 | 0.42 |
| 11-17 04:03 | +10 stop | SOL | DOWN | 0.59 | 0.44 | -1.85 |
| 11-17 04:03 | +10 stop | BNB | DOWN | 0.70 | 0.83 | 1.05 |
| 11-17 04:03 | +5 | BNB | DOWN | 0.70 | 0.78 | 0.52 |
| 11-17 04:03 | +10 stop | ETH | DOWN | 0.71 | 0.84 | 1.05 |
| 11-17 04:03 | +10 stop | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-17 04:03 | +20 | HYPE | DOWN | 0.71 | 0.91 | 1.83 |
| 11-17 04:03 | +15 | HYPE | DOWN | 0.71 | 0.88 | 1.47 |
| 11-17 04:03 | +10 | HYPE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-17 04:03 | +5 | HYPE | DOWN | 0.71 | 0.80 | 0.63 |
| 11-17 04:03 | +5 | BNB | DOWN | 0.64 | 0.69 | 0.18 |
| 11-17 04:03 | +5 | SOL | UP | 0.50 | 0.55 | 0.14 |
| 11-17 04:02 | +10 stop | XRP | DOWN | 0.70 | 0.83 | 1.05 |
| 11-17 04:02 | +5 | SOL | UP | 0.56 | 0.63 | 0.35 |
| 11-17 04:02 | +10 stop | ETH | UP | 0.52 | 0.37 | -1.85 |
| 11-17 04:02 | +20 | ETH | UP | 0.51 | open |  |
| 11-17 04:02 | +15 | ETH | UP | 0.53 | open |  |
| 11-17 04:02 | +10 | ETH | UP | 0.53 | open |  |
| 11-17 04:02 | +5 | ETH | UP | 0.53 | open |  |
| 11-17 04:01 | +10 stop | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 11-17 04:01 | +20 | DOGE | DOWN | 0.58 | 0.78 | 1.69 |
| 11-17 04:01 | +15 | DOGE | DOWN | 0.58 | 0.74 | 1.28 |
| 11-17 04:01 | +10 | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 11-17 04:01 | +5 | DOGE | DOWN | 0.58 | 0.70 | 0.87 |
| 11-17 04:01 | +10 stop | SOL | UP | 0.62 | 0.41 | -2.44 |
| 11-17 04:01 | +20 | SOL | UP | 0.61 | 0.84 | 2.03 |
| 11-17 04:01 | +15 | SOL | UP | 0.62 | 0.77 | 1.20 |
| 11-17 04:01 | +10 | SOL | UP | 0.59 | 0.77 | 1.50 |
| 11-17 04:01 | +5 | SOL | UP | 0.59 | 0.65 | 0.27 |
| 11-17 04:01 | +10 stop | BNB | UP | 0.49 | 0.30 | -2.23 |
| 11-17 04:01 | +20 | BNB | UP | 0.49 | open |  |
| 11-17 04:01 | +15 | BNB | UP | 0.49 | open |  |
| 11-17 04:01 | +10 | BNB | UP | 0.49 | open |  |
| 11-17 04:01 | +5 | BNB | UP | 0.49 | 0.55 | 0.24 |
| 11-17 04:01 | +10 stop | BTC | DOWN | 0.55 | 0.70 | 1.17 |
| 11-17 04:01 | +20 | BTC | DOWN | 0.55 | 0.75 | 1.68 |
| 11-17 04:01 | +15 | BTC | DOWN | 0.55 | 0.70 | 1.17 |
| 11-17 04:01 | +10 | BTC | DOWN | 0.55 | 0.70 | 1.17 |
