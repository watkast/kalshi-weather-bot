# Range-Scalp Bot

*Updated Tue Nov 03 14:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46044 | 40090 | 5954 (70) | 0 | $-13286.93 | -4.6% |
| **+10¢** | 34372 | 27476 | 6896 (92) | 2 | $-12144.60 | -5.6% |
| **+15¢** | 28767 | 21352 | 7415 (120) | 2 | $-11088.87 | -6.1% |
| **+20¢** | 25553 | 17782 | 7771 (157) | 2 | $-9852.02 | -6.1% |
| **+10¢ (15¢ stop)** | 56168 | 56079 | 89 (53) | 0 | $-21042.76 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 14:08 | +10 stop | HYPE | DOWN | 0.57 | 0.41 | -1.95 |
| 11-03 14:08 | +5 | HYPE | DOWN | 0.54 | 0.59 | 0.15 |
| 11-03 14:07 | +10 stop | HYPE | UP | 0.55 | 0.36 | -2.25 |
| 11-03 14:07 | +20 | HYPE | UP | 0.53 | open |  |
| 11-03 14:07 | +15 | HYPE | UP | 0.53 | open |  |
| 11-03 14:07 | +10 | HYPE | UP | 0.53 | open |  |
| 11-03 14:07 | +5 | HYPE | UP | 0.53 | 0.60 | 0.35 |
| 11-03 14:04 | +10 stop | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 11-03 14:04 | +5 | NEAR | DOWN | 0.64 | 0.75 | 0.79 |
| 11-03 14:02 | +5 | NEAR | DOWN | 0.69 | 0.83 | 1.15 |
| 11-03 14:02 | +10 stop | SOL | DOWN | 0.68 | 0.83 | 1.24 |
| 11-03 14:02 | +10 | SOL | DOWN | 0.68 | 0.83 | 1.24 |
| 11-03 14:02 | +5 | SOL | DOWN | 0.67 | 0.83 | 1.34 |
| 11-03 14:01 | +10 stop | NEAR | UP | 0.55 | 0.31 | -2.73 |
| 11-03 14:01 | +20 | NEAR | UP | 0.55 | open |  |
| 11-03 14:01 | +15 | NEAR | UP | 0.55 | open |  |
| 11-03 14:01 | +10 | NEAR | UP | 0.55 | open |  |
| 11-03 14:01 | +5 | NEAR | UP | 0.55 | 0.64 | 0.55 |
| 11-03 14:01 | +5 | ETH | DOWN | 0.59 | 0.74 | 1.19 |
| 11-03 14:01 | +5 | BTC | DOWN | 0.60 | 0.68 | 0.47 |
| 11-03 14:00 | +10 stop | ETH | DOWN | 0.53 | 0.74 | 1.78 |
| 11-03 14:00 | +20 | ETH | DOWN | 0.53 | 0.74 | 1.78 |
| 11-03 14:00 | +15 | ETH | DOWN | 0.53 | 0.74 | 1.78 |
| 11-03 14:00 | +10 | ETH | DOWN | 0.53 | 0.74 | 1.78 |
| 11-03 14:00 | +5 | ETH | DOWN | 0.53 | 0.58 | 0.14 |
| 11-03 14:00 | +10 stop | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 11-03 14:00 | +20 | BNB | DOWN | 0.62 | 0.85 | 2.04 |
| 11-03 14:00 | +15 | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 11-03 14:00 | +10 | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 11-03 14:00 | +5 | BNB | DOWN | 0.62 | 0.80 | 1.51 |
| 11-03 14:00 | +10 stop | BTC | DOWN | 0.55 | 0.68 | 0.96 |
| 11-03 14:00 | +20 | BTC | DOWN | 0.55 | 0.76 | 1.79 |
| 11-03 14:00 | +15 | BTC | DOWN | 0.55 | 0.70 | 1.17 |
| 11-03 14:00 | +10 | BTC | DOWN | 0.55 | 0.68 | 0.96 |
| 11-03 14:00 | +5 | BTC | DOWN | 0.55 | 0.61 | 0.25 |
| 11-03 14:00 | +10 stop | SOL | DOWN | 0.49 | 0.59 | 0.65 |
| 11-03 14:00 | +20 | SOL | DOWN | 0.49 | 0.69 | 1.67 |
| 11-03 14:00 | +15 | SOL | DOWN | 0.49 | 0.67 | 1.46 |
| 11-03 14:00 | +10 | SOL | DOWN | 0.49 | 0.59 | 0.65 |
| 11-03 14:00 | +5 | SOL | DOWN | 0.49 | 0.55 | 0.24 |
