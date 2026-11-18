# Range-Scalp Bot

*Updated Wed Nov 18 17:55 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64295 | 56073 | 8222 (124) | 0 | $-17580.58 | -4.3% |
| **+10¢** | 48024 | 38406 | 9618 (165) | 0 | $-16439.60 | -5.4% |
| **+15¢** | 40263 | 29898 | 10365 (210) | 0 | $-14865.24 | -5.9% |
| **+20¢** | 35853 | 24974 | 10879 (265) | 0 | $-13156.68 | -5.8% |
| **+10¢ (15¢ stop)** | 78217 | 78053 | 164 (98) | 0 | $-28796.18 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 17:48 | +10 stop | BTC | DOWN | 0.54 | 0.71 | 1.37 |
| 11-18 17:48 | +10 stop | BNB | DOWN | 0.61 | 0.84 | 2.03 |
| 11-18 17:48 | +10 stop | ZEC | DOWN | 0.65 | 0.84 | 1.67 |
| 11-18 17:47 | +5 | HYPE | DOWN | 0.61 | 0.75 | 1.09 |
| 11-18 17:47 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 11-18 17:47 | +5 | HYPE | DOWN | 0.52 | 0.57 | 0.14 |
| 11-18 17:46 | +10 stop | BTC | DOWN | 0.68 | 0.49 | -2.24 |
| 11-18 17:46 | +20 | BTC | DOWN | 0.68 | 0.88 | 1.76 |
| 11-18 17:46 | +15 | BTC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-18 17:46 | +10 | BTC | DOWN | 0.68 | 0.80 | 0.92 |
| 11-18 17:46 | +5 | BTC | DOWN | 0.68 | 0.75 | 0.40 |
| 11-18 17:46 | +10 stop | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 11-18 17:46 | +20 | NEAR | DOWN | 0.68 | 0.91 | 2.05 |
| 11-18 17:46 | +15 | NEAR | DOWN | 0.68 | 0.87 | 1.66 |
| 11-18 17:46 | +10 | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 11-18 17:46 | +5 | NEAR | DOWN | 0.68 | 0.80 | 0.92 |
| 11-18 17:46 | +10 stop | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-18 17:46 | +20 | ETH | DOWN | 0.70 | 0.90 | 1.82 |
| 11-18 17:46 | +15 | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 11-18 17:46 | +10 | ETH | DOWN | 0.70 | 0.82 | 0.94 |
| 11-18 17:46 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 11-18 17:46 | +10 stop | SOL | DOWN | 0.70 | 0.87 | 1.47 |
| 11-18 17:46 | +20 | SOL | DOWN | 0.70 | 0.91 | 1.90 |
| 11-18 17:46 | +15 | SOL | DOWN | 0.70 | 0.87 | 1.47 |
| 11-18 17:46 | +10 | SOL | DOWN | 0.71 | 0.87 | 1.37 |
| 11-18 17:46 | +5 | SOL | DOWN | 0.71 | 0.78 | 0.42 |
| 11-18 17:46 | +10 stop | XRP | DOWN | 0.69 | 0.83 | 1.15 |
| 11-18 17:46 | +20 | XRP | DOWN | 0.69 | 0.89 | 1.78 |
| 11-18 17:46 | +15 | XRP | DOWN | 0.69 | 0.86 | 1.46 |
| 11-18 17:46 | +10 | XRP | DOWN | 0.69 | 0.83 | 1.15 |
| 11-18 17:46 | +5 | XRP | DOWN | 0.69 | 0.75 | 0.31 |
| 11-18 17:46 | +10 stop | BNB | DOWN | 0.66 | 0.49 | -2.04 |
| 11-18 17:46 | +20 | BNB | DOWN | 0.66 | 0.88 | 1.96 |
| 11-18 17:46 | +15 | BNB | DOWN | 0.66 | 0.84 | 1.54 |
| 11-18 17:46 | +10 | BNB | DOWN | 0.66 | 0.84 | 1.54 |
| 11-18 17:46 | +5 | BNB | DOWN | 0.66 | 0.84 | 1.54 |
| 11-18 17:46 | +10 stop | DOGE | DOWN | 0.64 | 0.78 | 1.10 |
| 11-18 17:46 | +20 | DOGE | DOWN | 0.64 | 0.86 | 1.94 |
| 11-18 17:46 | +15 | DOGE | DOWN | 0.65 | 0.86 | 1.85 |
| 11-18 17:46 | +10 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
