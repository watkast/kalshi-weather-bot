# Range-Scalp Bot

*Updated Tue Nov 17 15:06 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62934 | 54897 | 8037 (117) | 1 | $-17134.28 | -4.3% |
| **+10¢** | 47002 | 37598 | 9404 (159) | 1 | $-16008.60 | -5.4% |
| **+15¢** | 39396 | 29254 | 10142 (201) | 0 | $-14540.72 | -5.9% |
| **+20¢** | 35107 | 24472 | 10635 (256) | 0 | $-12714.13 | -5.8% |
| **+10¢ (15¢ stop)** | 76579 | 76423 | 156 (92) | 0 | $-28221.27 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 15:04 | +20 | XRP | DOWN | 0.68 | 0.91 | 2.02 |
| 11-17 15:04 | +5 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-17 15:04 | +10 stop | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 11-17 15:04 | +10 | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 11-17 15:04 | +5 | NEAR | DOWN | 0.65 | 0.80 | 1.22 |
| 11-17 15:04 | +10 stop | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 11-17 15:04 | +15 | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 11-17 15:04 | +10 | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 11-17 15:04 | +5 | ETH | DOWN | 0.70 | 0.77 | 0.42 |
| 11-17 15:03 | +10 stop | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 11-17 15:03 | +15 | BNB | DOWN | 0.63 | 0.81 | 1.52 |
| 11-17 15:03 | +10 | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 11-17 15:03 | +5 | DOGE | DOWN | 0.66 | 0.71 | 0.19 |
| 11-17 15:03 | +10 stop | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-17 15:03 | +10 | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 11-17 15:03 | +15 | XRP | DOWN | 0.60 | 0.84 | 2.13 |
| 11-17 15:03 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
| 11-17 15:03 | +10 stop | XRP | DOWN | 0.62 | 0.72 | 0.68 |
| 11-17 15:03 | +5 | HYPE | DOWN | 0.71 | 0.78 | 0.42 |
| 11-17 15:02 | +5 | SOL | DOWN | 0.69 | 0.78 | 0.62 |
| 11-17 15:02 | +10 stop | XRP | UP | 0.67 | 0.50 | -2.04 |
| 11-17 15:02 | +10 | XRP | UP | 0.69 | open |  |
| 11-17 15:02 | +5 | XRP | UP | 0.69 | open |  |
| 11-17 15:02 | +5 | BTC | DOWN | 0.57 | 0.66 | 0.56 |
| 11-17 15:01 | +5 | ETH | DOWN | 0.60 | 0.71 | 0.78 |
| 11-17 15:01 | +10 stop | DOGE | DOWN | 0.61 | 0.71 | 0.68 |
| 11-17 15:01 | +20 | DOGE | DOWN | 0.61 | 0.86 | 2.24 |
| 11-17 15:01 | +15 | DOGE | DOWN | 0.61 | 0.77 | 1.30 |
| 11-17 15:01 | +10 | DOGE | DOWN | 0.61 | 0.71 | 0.68 |
| 11-17 15:01 | +5 | DOGE | DOWN | 0.62 | 0.68 | 0.27 |
| 11-17 15:01 | +10 stop | NEAR | DOWN | 0.58 | 0.70 | 0.87 |
| 11-17 15:01 | +20 | NEAR | DOWN | 0.59 | 0.80 | 1.81 |
| 11-17 15:01 | +15 | NEAR | DOWN | 0.58 | 0.80 | 1.90 |
| 11-17 15:01 | +10 | NEAR | DOWN | 0.58 | 0.70 | 0.87 |
| 11-17 15:01 | +5 | NEAR | DOWN | 0.57 | 0.66 | 0.52 |
| 11-17 15:01 | +10 stop | SOL | DOWN | 0.58 | 0.70 | 0.87 |
| 11-17 15:01 | +20 | SOL | DOWN | 0.58 | 0.78 | 1.69 |
| 11-17 15:01 | +15 | SOL | DOWN | 0.59 | 0.78 | 1.61 |
| 11-17 15:01 | +10 | SOL | DOWN | 0.59 | 0.70 | 0.79 |
| 11-17 15:01 | +5 | SOL | DOWN | 0.59 | 0.64 | 0.17 |
