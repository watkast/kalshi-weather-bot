# Range-Scalp Bot

*Updated Tue Nov 17 00:05 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62456 | 54487 | 7969 (117) | 0 | $-16922.64 | -4.3% |
| **+10¢** | 46647 | 37322 | 9325 (159) | 0 | $-15794.55 | -5.4% |
| **+15¢** | 39093 | 29035 | 10058 (201) | 0 | $-14354.07 | -5.9% |
| **+20¢** | 34843 | 24294 | 10549 (256) | 1 | $-12544.88 | -5.7% |
| **+10¢ (15¢ stop)** | 76008 | 75852 | 156 (92) | 0 | $-28019.70 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-17 00:03 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-17 00:02 | +10 stop | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-17 00:02 | +10 | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-17 00:02 | +5 | BTC | DOWN | 0.70 | 0.78 | 0.52 |
| 11-17 00:02 | +5 | DOGE | DOWN | 0.66 | 0.72 | 0.29 |
| 11-17 00:02 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
| 11-17 00:02 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-17 00:02 | +20 | ETH | DOWN | 0.65 | 0.87 | 1.96 |
| 11-17 00:02 | +15 | ETH | DOWN | 0.65 | 0.81 | 1.33 |
| 11-17 00:02 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-17 00:02 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.29 |
| 11-17 00:02 | +10 stop | BNB | DOWN | 0.62 | 0.78 | 1.30 |
| 11-17 00:02 | +20 | BNB | DOWN | 0.62 | 0.82 | 1.72 |
| 11-17 00:02 | +15 | BNB | DOWN | 0.62 | 0.78 | 1.30 |
| 11-17 00:02 | +10 | BNB | DOWN | 0.62 | 0.78 | 1.30 |
| 11-17 00:02 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 11-17 00:01 | +10 stop | DOGE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-17 00:01 | +20 | DOGE | DOWN | 0.58 | 0.83 | 2.22 |
| 11-17 00:01 | +15 | DOGE | DOWN | 0.58 | 0.76 | 1.49 |
| 11-17 00:01 | +10 | DOGE | DOWN | 0.58 | 0.69 | 0.77 |
| 11-17 00:01 | +5 | DOGE | DOWN | 0.59 | 0.65 | 0.27 |
| 11-17 00:01 | +10 stop | HYPE | DOWN | 0.63 | 0.73 | 0.69 |
| 11-17 00:01 | +20 | HYPE | DOWN | 0.62 | 0.84 | 1.93 |
| 11-17 00:01 | +15 | HYPE | DOWN | 0.63 | 0.84 | 1.83 |
| 11-17 00:01 | +10 | HYPE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-17 00:01 | +5 | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 11-17 00:01 | +10 stop | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 11-17 00:01 | +20 | XRP | DOWN | 0.59 | 0.79 | 1.71 |
| 11-17 00:01 | +15 | XRP | DOWN | 0.59 | 0.77 | 1.50 |
| 11-17 00:01 | +10 | XRP | DOWN | 0.59 | 0.69 | 0.68 |
| 11-17 00:01 | +5 | XRP | DOWN | 0.59 | 0.65 | 0.27 |
| 11-17 00:01 | +10 stop | SOL | DOWN | 0.57 | 0.68 | 0.76 |
| 11-17 00:01 | +20 | SOL | DOWN | 0.57 | 0.78 | 1.79 |
| 11-17 00:01 | +15 | SOL | DOWN | 0.57 | 0.74 | 1.38 |
| 11-17 00:01 | +10 | SOL | DOWN | 0.57 | 0.68 | 0.76 |
| 11-17 00:01 | +5 | SOL | DOWN | 0.57 | 0.63 | 0.25 |
| 11-17 00:01 | +10 stop | BTC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-17 00:01 | +20 | BTC | DOWN | 0.58 | 0.78 | 1.69 |
| 11-17 00:01 | +15 | BTC | DOWN | 0.58 | 0.74 | 1.28 |
| 11-17 00:01 | +10 | BTC | DOWN | 0.58 | 0.68 | 0.66 |
