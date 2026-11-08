# Range-Scalp Bot

*Updated Sun Nov 08 04:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52015 | 45358 | 6657 (80) | 0 | $-14394.97 | -4.4% |
| **+10¢** | 38821 | 31055 | 7766 (106) | 0 | $-13421.58 | -5.5% |
| **+15¢** | 32511 | 24143 | 8368 (135) | 0 | $-12291.20 | -6.0% |
| **+20¢** | 28919 | 20147 | 8772 (180) | 2 | $-10822.66 | -6.0% |
| **+10¢ (15¢ stop)** | 63320 | 63217 | 103 (61) | 0 | $-23408.86 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 04:54 | +10 stop | XRP | DOWN | 0.63 | 0.76 | 1.00 |
| 11-08 04:54 | +10 | XRP | DOWN | 0.63 | 0.76 | 1.00 |
| 11-08 04:53 | +5 | XRP | DOWN | 0.63 | 0.76 | 1.00 |
| 11-08 04:51 | +10 stop | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 11-08 04:51 | +15 | SOL | DOWN | 0.64 | 0.80 | 1.31 |
| 11-08 04:51 | +10 | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 11-08 04:51 | +5 | SOL | DOWN | 0.64 | 0.75 | 0.79 |
| 11-08 04:51 | +10 stop | XRP | DOWN | 0.54 | 0.65 | 0.76 |
| 11-08 04:51 | +15 | XRP | DOWN | 0.54 | 0.76 | 1.89 |
| 11-08 04:51 | +10 | XRP | DOWN | 0.54 | 0.65 | 0.76 |
| 11-08 04:51 | +5 | XRP | DOWN | 0.54 | 0.62 | 0.45 |
| 11-08 04:47 | +5 | HYPE | DOWN | 0.64 | 0.78 | 1.10 |
| 11-08 04:47 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-08 04:47 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 11-08 04:47 | +20 | ETH | DOWN | 0.71 | 0.92 | 1.85 |
| 11-08 04:47 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 11-08 04:47 | +10 | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 11-08 04:47 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 11-08 04:46 | +10 stop | NEAR | DOWN | 0.70 | 0.89 | 1.68 |
| 11-08 04:46 | +20 | NEAR | DOWN | 0.68 | 0.89 | 1.87 |
| 11-08 04:46 | +15 | NEAR | DOWN | 0.68 | 0.89 | 1.87 |
| 11-08 04:46 | +10 | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 11-08 04:46 | +5 | NEAR | DOWN | 0.67 | 0.76 | 0.61 |
| 11-08 04:46 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 11-08 04:46 | +20 | XRP | DOWN | 0.68 | open |  |
| 11-08 04:46 | +15 | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 11-08 04:46 | +10 | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 11-08 04:46 | +5 | XRP | DOWN | 0.68 | 0.73 | 0.20 |
| 11-08 04:46 | +10 stop | HYPE | DOWN | 0.69 | 0.82 | 1.04 |
| 11-08 04:46 | +20 | HYPE | DOWN | 0.69 | 0.89 | 1.78 |
| 11-08 04:46 | +15 | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-08 04:46 | +10 | HYPE | DOWN | 0.69 | 0.82 | 1.04 |
| 11-08 04:46 | +5 | HYPE | DOWN | 0.69 | 0.76 | 0.42 |
| 11-08 04:46 | +10 stop | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-08 04:46 | +20 | BTC | DOWN | 0.61 | 0.81 | 1.72 |
| 11-08 04:46 | +15 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-08 04:46 | +10 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-08 04:46 | +5 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-08 04:46 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-08 04:46 | +20 | SOL | DOWN | 0.67 | open |  |
