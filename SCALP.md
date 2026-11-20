# Range-Scalp Bot

*Updated Fri Nov 20 14:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66268 | 57828 | 8440 (128) | 0 | $-17861.64 | -4.3% |
| **+10¢** | 49488 | 39618 | 9870 (170) | 0 | $-16642.73 | -5.4% |
| **+15¢** | 41501 | 30857 | 10644 (217) | 0 | $-14991.91 | -5.8% |
| **+20¢** | 36950 | 25771 | 11179 (273) | 0 | $-13296.46 | -5.7% |
| **+10¢ (15¢ stop)** | 80719 | 80553 | 166 (100) | 0 | $-29830.22 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 14:32 | +10 | SOL | DOWN | 0.71 | 0.83 | 0.95 |
| 11-20 14:32 | +5 | SOL | DOWN | 0.63 | 0.70 | 0.38 |
| 11-20 14:32 | +5 | DOGE | DOWN | 0.69 | 0.78 | 0.64 |
| 11-20 14:32 | +10 stop | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 11-20 14:32 | +20 | BNB | DOWN | 0.65 | 0.85 | 1.75 |
| 11-20 14:32 | +15 | BNB | DOWN | 0.65 | 0.81 | 1.33 |
| 11-20 14:32 | +10 | BNB | DOWN | 0.65 | 0.77 | 0.91 |
| 11-20 14:32 | +5 | BNB | DOWN | 0.65 | 0.72 | 0.39 |
| 11-20 14:32 | +10 stop | ETH | DOWN | 0.68 | 0.81 | 1.03 |
| 11-20 14:32 | +20 | ETH | DOWN | 0.69 | 0.89 | 1.78 |
| 11-20 14:32 | +15 | ETH | DOWN | 0.69 | 0.85 | 1.36 |
| 11-20 14:32 | +10 | ETH | DOWN | 0.69 | 0.81 | 0.94 |
| 11-20 14:32 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 11-20 14:31 | +10 stop | HYPE | DOWN | 0.67 | 0.82 | 1.23 |
| 11-20 14:31 | +20 | HYPE | DOWN | 0.66 | 0.87 | 1.86 |
| 11-20 14:31 | +15 | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-20 14:31 | +10 | HYPE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-20 14:31 | +5 | HYPE | DOWN | 0.66 | 0.75 | 0.60 |
| 11-20 14:31 | +5 | DOGE | DOWN | 0.57 | 0.64 | 0.35 |
| 11-20 14:31 | +10 stop | XRP | DOWN | 0.61 | 0.73 | 0.92 |
| 11-20 14:31 | +20 | XRP | DOWN | 0.60 | 0.82 | 1.92 |
| 11-20 14:31 | +15 | XRP | DOWN | 0.60 | 0.82 | 1.92 |
| 11-20 14:31 | +10 | XRP | DOWN | 0.61 | 0.73 | 0.92 |
| 11-20 14:31 | +5 | XRP | DOWN | 0.61 | 0.67 | 0.30 |
| 11-20 14:31 | +10 stop | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-20 14:31 | +20 | ZEC | DOWN | 0.61 | 0.90 | 2.67 |
| 11-20 14:31 | +15 | ZEC | DOWN | 0.61 | 0.77 | 1.30 |
| 11-20 14:31 | +10 | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-20 14:31 | +5 | ZEC | DOWN | 0.62 | 0.71 | 0.58 |
| 11-20 14:31 | +10 stop | SOL | DOWN | 0.56 | 0.70 | 1.10 |
| 11-20 14:31 | +20 | SOL | DOWN | 0.56 | 0.83 | 2.42 |
| 11-20 14:31 | +15 | SOL | DOWN | 0.56 | 0.83 | 2.39 |
| 11-20 14:31 | +10 | SOL | DOWN | 0.55 | 0.65 | 0.68 |
| 11-20 14:31 | +5 | SOL | DOWN | 0.53 | 0.59 | 0.25 |
| 11-20 14:31 | +10 stop | NEAR | DOWN | 0.57 | 0.70 | 0.97 |
| 11-20 14:31 | +20 | NEAR | DOWN | 0.57 | 0.84 | 2.42 |
| 11-20 14:31 | +15 | NEAR | DOWN | 0.57 | 0.74 | 1.38 |
| 11-20 14:31 | +10 | NEAR | DOWN | 0.57 | 0.70 | 0.93 |
| 11-20 14:31 | +5 | NEAR | DOWN | 0.57 | 0.70 | 0.93 |
| 11-20 14:31 | +10 stop | DOGE | DOWN | 0.55 | 0.72 | 1.37 |
