# Range-Scalp Bot

*Updated Mon Nov 16 01:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61484 | 53655 | 7829 (115) | 2 | $-16523.39 | -4.3% |
| **+10¢** | 45925 | 36751 | 9174 (156) | 1 | $-15488.11 | -5.4% |
| **+15¢** | 38476 | 28578 | 9898 (195) | 1 | $-14129.75 | -5.9% |
| **+20¢** | 34297 | 23914 | 10383 (247) | 1 | $-12382.39 | -5.8% |
| **+10¢ (15¢ stop)** | 74819 | 74665 | 154 (90) | 0 | $-27493.99 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 01:21 | +10 | ZEC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-16 01:21 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-16 01:20 | +10 stop | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-16 01:20 | +5 | NEAR | DOWN | 0.70 | 0.77 | 0.42 |
| 11-16 01:20 | +10 stop | BNB | DOWN | 0.61 | 0.71 | 0.68 |
| 11-16 01:19 | +10 stop | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 11-16 01:19 | +10 stop | ZEC | UP | 0.58 | 0.38 | -2.35 |
| 11-16 01:18 | +10 stop | BTC | UP | 0.54 | 0.36 | -2.15 |
| 11-16 01:18 | +20 | BTC | UP | 0.54 | open |  |
| 11-16 01:18 | +15 | BTC | UP | 0.54 | open |  |
| 11-16 01:18 | +10 | BTC | UP | 0.55 | open |  |
| 11-16 01:18 | +5 | BTC | UP | 0.55 | open |  |
| 11-16 01:18 | +5 | ZEC | UP | 0.59 | open |  |
| 11-16 01:18 | +5 | NEAR | DOWN | 0.61 | 0.67 | 0.27 |
| 11-16 01:18 | +10 stop | ETH | DOWN | 0.54 | 0.69 | 1.17 |
| 11-16 01:18 | +10 stop | NEAR | DOWN | 0.60 | 0.71 | 0.79 |
| 11-16 01:18 | +20 | NEAR | DOWN | 0.60 | 0.86 | 2.36 |
| 11-16 01:18 | +15 | NEAR | DOWN | 0.59 | 0.77 | 1.50 |
| 11-16 01:18 | +10 | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 11-16 01:18 | +5 | NEAR | DOWN | 0.59 | 0.66 | 0.37 |
| 11-16 01:18 | +10 stop | BNB | DOWN | 0.54 | 0.39 | -1.85 |
| 11-16 01:16 | +10 stop | HYPE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-16 01:16 | +20 | HYPE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-16 01:16 | +15 | HYPE | DOWN | 0.64 | 0.80 | 1.36 |
| 11-16 01:16 | +10 | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-16 01:16 | +5 | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-16 01:16 | +10 stop | ETH | DOWN | 0.63 | 0.46 | -2.05 |
| 11-16 01:16 | +20 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
| 11-16 01:16 | +15 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
| 11-16 01:16 | +10 | ETH | DOWN | 0.63 | 0.77 | 1.10 |
| 11-16 01:16 | +5 | ETH | DOWN | 0.63 | 0.69 | 0.28 |
| 11-16 01:16 | +10 stop | DOGE | DOWN | 0.60 | 0.71 | 0.78 |
| 11-16 01:16 | +20 | DOGE | DOWN | 0.60 | 0.80 | 1.71 |
| 11-16 01:16 | +15 | DOGE | DOWN | 0.60 | 0.75 | 1.19 |
| 11-16 01:16 | +10 | DOGE | DOWN | 0.61 | 0.71 | 0.68 |
| 11-16 01:16 | +5 | DOGE | DOWN | 0.61 | 0.71 | 0.68 |
| 11-16 01:16 | +10 stop | SOL | DOWN | 0.62 | 0.44 | -2.15 |
| 11-16 01:16 | +20 | SOL | DOWN | 0.62 | 0.82 | 1.72 |
| 11-16 01:16 | +15 | SOL | DOWN | 0.62 | 0.79 | 1.41 |
| 11-16 01:16 | +10 | SOL | DOWN | 0.62 | 0.79 | 1.41 |
