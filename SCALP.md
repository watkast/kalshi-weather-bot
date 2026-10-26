# Range-Scalp Bot

*Updated Mon Oct 26 18:51 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35260 | 30783 | 4477 (43) | 0 | $-9794.99 | -4.4% |
| **+10¢** | 26382 | 21207 | 5175 (65) | 0 | $-8585.31 | -5.2% |
| **+15¢** | 22074 | 16502 | 5572 (89) | 0 | $-7685.91 | -5.5% |
| **+20¢** | 19576 | 13738 | 5838 (112) | 2 | $-6719.89 | -5.5% |
| **+10¢ (15¢ stop)** | 43212 | 43150 | 62 (33) | 0 | $-16430.12 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 18:48 | +5 | ZEC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-26 18:48 | +5 | BTC | DOWN | 0.61 | 0.69 | 0.48 |
| 10-26 18:48 | +10 stop | NEAR | DOWN | 0.66 | 0.79 | 1.02 |
| 10-26 18:48 | +10 | NEAR | DOWN | 0.66 | 0.79 | 1.02 |
| 10-26 18:48 | +5 | NEAR | DOWN | 0.66 | 0.74 | 0.53 |
| 10-26 18:48 | +10 stop | ETH | DOWN | 0.59 | 0.72 | 0.98 |
| 10-26 18:48 | +10 | ETH | DOWN | 0.59 | 0.72 | 0.98 |
| 10-26 18:48 | +5 | ETH | DOWN | 0.59 | 0.68 | 0.57 |
| 10-26 18:48 | +10 stop | SOL | DOWN | 0.71 | 0.82 | 0.84 |
| 10-26 18:48 | +10 stop | XRP | DOWN | 0.62 | 0.76 | 1.10 |
| 10-26 18:48 | +10 stop | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 10-26 18:48 | +20 | DOGE | DOWN | 0.66 | open |  |
| 10-26 18:48 | +15 | DOGE | DOWN | 0.66 | 0.84 | 1.54 |
| 10-26 18:48 | +10 | DOGE | DOWN | 0.66 | 0.76 | 0.71 |
| 10-26 18:48 | +5 | DOGE | DOWN | 0.66 | 0.75 | 0.60 |
| 10-26 18:47 | +10 stop | NEAR | UP | 0.49 | 0.59 | 0.65 |
| 10-26 18:47 | +10 | NEAR | UP | 0.49 | 0.59 | 0.65 |
| 10-26 18:47 | +5 | NEAR | UP | 0.50 | 0.59 | 0.55 |
| 10-26 18:47 | +10 stop | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 10-26 18:47 | +20 | BNB | DOWN | 0.63 | 0.84 | 1.83 |
| 10-26 18:47 | +15 | BNB | DOWN | 0.63 | 0.84 | 1.83 |
| 10-26 18:47 | +10 | BNB | DOWN | 0.63 | 0.74 | 0.79 |
| 10-26 18:47 | +5 | BNB | DOWN | 0.63 | 0.70 | 0.38 |
| 10-26 18:47 | +5 | BTC | DOWN | 0.56 | 0.61 | 0.15 |
| 10-26 18:47 | +10 stop | HYPE | DOWN | 0.57 | 0.70 | 0.97 |
| 10-26 18:47 | +20 | HYPE | DOWN | 0.57 | 0.77 | 1.69 |
| 10-26 18:47 | +15 | HYPE | DOWN | 0.57 | 0.72 | 1.17 |
| 10-26 18:47 | +10 | HYPE | DOWN | 0.57 | 0.70 | 0.97 |
| 10-26 18:47 | +5 | HYPE | DOWN | 0.57 | 0.62 | 0.15 |
| 10-26 18:47 | +10 stop | NEAR | DOWN | 0.52 | 0.64 | 0.85 |
| 10-26 18:47 | +20 | NEAR | DOWN | 0.52 | 0.74 | 1.88 |
| 10-26 18:47 | +15 | NEAR | DOWN | 0.52 | 0.69 | 1.37 |
| 10-26 18:47 | +10 | NEAR | DOWN | 0.52 | 0.64 | 0.85 |
| 10-26 18:47 | +5 | NEAR | DOWN | 0.52 | 0.64 | 0.85 |
| 10-26 18:47 | +10 stop | ETH | DOWN | 0.53 | 0.63 | 0.65 |
| 10-26 18:47 | +20 | ETH | DOWN | 0.53 | 0.79 | 2.30 |
| 10-26 18:47 | +15 | ETH | DOWN | 0.53 | 0.68 | 1.16 |
| 10-26 18:47 | +10 | ETH | DOWN | 0.53 | 0.63 | 0.65 |
| 10-26 18:47 | +5 | ETH | DOWN | 0.53 | 0.63 | 0.65 |
| 10-26 18:46 | +10 stop | BTC | DOWN | 0.62 | 0.72 | 0.68 |
