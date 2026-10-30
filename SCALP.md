# Range-Scalp Bot

*Updated Fri Oct 30 18:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 41142 | 35915 | 5227 (53) | 0 | $-11446.74 | -4.4% |
| **+10¢** | 30665 | 24618 | 6047 (76) | 0 | $-10168.39 | -5.3% |
| **+15¢** | 25633 | 19118 | 6515 (103) | 0 | $-9218.84 | -5.7% |
| **+20¢** | 22752 | 15928 | 6824 (133) | 1 | $-8103.29 | -5.7% |
| **+10¢ (15¢ stop)** | 50161 | 50091 | 70 (37) | 0 | $-18946.85 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 18:50 | +10 stop | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-30 18:50 | +5 | ZEC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-30 18:50 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 10-30 18:49 | +10 | XRP | DOWN | 0.68 | 0.85 | 1.45 |
| 10-30 18:49 | +5 | XRP | DOWN | 0.68 | 0.76 | 0.51 |
| 10-30 18:49 | +10 | BTC | DOWN | 0.55 | 0.67 | 0.86 |
| 10-30 18:49 | +10 stop | ETH | DOWN | 0.67 | 0.84 | 1.44 |
| 10-30 18:49 | +15 | ETH | DOWN | 0.67 | 0.84 | 1.44 |
| 10-30 18:49 | +10 | ETH | DOWN | 0.67 | 0.84 | 1.44 |
| 10-30 18:48 | +10 stop | SOL | DOWN | 0.66 | 0.80 | 1.12 |
| 10-30 18:48 | +20 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 10-30 18:48 | +15 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 10-30 18:48 | +10 | SOL | DOWN | 0.66 | 0.80 | 1.12 |
| 10-30 18:48 | +5 | SOL | DOWN | 0.66 | 0.71 | 0.19 |
| 10-30 18:48 | +5 | BTC | DOWN | 0.69 | 0.78 | 0.62 |
| 10-30 18:48 | +5 | ETH | DOWN | 0.70 | 0.84 | 1.15 |
| 10-30 18:48 | +10 stop | BTC | DOWN | 0.67 | 0.78 | 0.81 |
| 10-30 18:48 | +10 stop | XRP | DOWN | 0.71 | 0.85 | 1.17 |
| 10-30 18:47 | +10 stop | ZEC | UP | 0.50 | 0.35 | -1.84 |
| 10-30 18:47 | +5 | HYPE | DOWN | 0.61 | 0.70 | 0.58 |
| 10-30 18:47 | +10 stop | BNB | DOWN | 0.69 | 0.80 | 0.79 |
| 10-30 18:47 | +10 | BNB | DOWN | 0.69 | 0.80 | 0.79 |
| 10-30 18:47 | +5 | HYPE | DOWN | 0.59 | 0.65 | 0.23 |
| 10-30 18:46 | +5 | BNB | DOWN | 0.71 | 0.80 | 0.63 |
| 10-30 18:46 | +10 stop | BTC | DOWN | 0.57 | 0.41 | -1.95 |
| 10-30 18:46 | +20 | BTC | DOWN | 0.57 | 0.78 | 1.79 |
| 10-30 18:46 | +15 | BTC | DOWN | 0.57 | 0.73 | 1.28 |
| 10-30 18:46 | +10 | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 10-30 18:46 | +5 | BTC | DOWN | 0.57 | 0.62 | 0.15 |
| 10-30 18:46 | +10 stop | XRP | DOWN | 0.62 | 0.46 | -1.95 |
| 10-30 18:46 | +20 | XRP | DOWN | 0.62 | 0.85 | 2.04 |
| 10-30 18:46 | +15 | XRP | DOWN | 0.62 | 0.85 | 2.04 |
| 10-30 18:46 | +10 | XRP | DOWN | 0.62 | 0.74 | 0.89 |
| 10-30 18:46 | +5 | XRP | DOWN | 0.62 | 0.67 | 0.17 |
| 10-30 18:46 | +10 stop | NEAR | DOWN | 0.54 | 0.67 | 0.96 |
| 10-30 18:46 | +20 | NEAR | DOWN | 0.54 | 0.74 | 1.68 |
| 10-30 18:46 | +15 | NEAR | DOWN | 0.54 | 0.70 | 1.27 |
| 10-30 18:46 | +10 | NEAR | DOWN | 0.54 | 0.67 | 0.96 |
| 10-30 18:46 | +5 | NEAR | DOWN | 0.54 | 0.61 | 0.35 |
| 10-30 18:46 | +10 stop | ETH | DOWN | 0.57 | 0.73 | 1.28 |
