# Range-Scalp Bot

*Updated Mon Nov 16 03:48 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61654 | 53803 | 7851 (115) | 0 | $-16559.83 | -4.3% |
| **+10¢** | 46054 | 36854 | 9200 (157) | 0 | $-15509.28 | -5.4% |
| **+15¢** | 38590 | 28667 | 9923 (196) | 0 | $-14128.41 | -5.8% |
| **+20¢** | 34399 | 23990 | 10409 (249) | 1 | $-12361.54 | -5.7% |
| **+10¢ (15¢ stop)** | 75033 | 74879 | 154 (90) | 0 | $-27624.47 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 03:46 | +10 stop | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-16 03:46 | +20 | BTC | DOWN | 0.66 | open |  |
| 11-16 03:46 | +15 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 11-16 03:46 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-16 03:46 | +5 | BTC | DOWN | 0.66 | 0.71 | 0.19 |
| 11-16 03:46 | +10 stop | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 11-16 03:46 | +20 | BNB | DOWN | 0.63 | 0.83 | 1.73 |
| 11-16 03:46 | +15 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 11-16 03:46 | +10 | BNB | DOWN | 0.63 | 0.78 | 1.20 |
| 11-16 03:46 | +5 | BNB | DOWN | 0.63 | 0.71 | 0.48 |
| 11-16 03:46 | +5 | ETH | DOWN | 0.71 | 0.78 | 0.42 |
| 11-16 03:45 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-16 03:45 | +20 | HYPE | DOWN | 0.68 | 0.88 | 1.76 |
| 11-16 03:45 | +15 | HYPE | DOWN | 0.68 | 0.84 | 1.34 |
| 11-16 03:45 | +10 | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-16 03:45 | +5 | HYPE | DOWN | 0.68 | 0.74 | 0.30 |
| 11-16 03:45 | +10 stop | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 11-16 03:45 | +20 | ETH | DOWN | 0.65 | 0.88 | 2.06 |
| 11-16 03:45 | +15 | ETH | DOWN | 0.65 | 0.81 | 1.33 |
| 11-16 03:45 | +10 | ETH | DOWN | 0.65 | 0.78 | 1.01 |
| 11-16 03:45 | +5 | ETH | DOWN | 0.65 | 0.70 | 0.19 |
| 11-16 03:43 | +5 | ZEC | DOWN | 0.58 | yes | -5.98 |
| 11-16 03:42 | +10 stop | ZEC | DOWN | 0.62 | 0.17 | -4.77 |
| 11-16 03:42 | +20 | ZEC | DOWN | 0.62 | yes | -6.37 |
| 11-16 03:42 | +15 | ZEC | DOWN | 0.62 | yes | -6.37 |
| 11-16 03:42 | +10 | ZEC | DOWN | 0.59 | yes | -6.07 |
| 11-16 03:42 | +5 | ZEC | DOWN | 0.59 | 0.67 | 0.47 |
| 11-16 03:41 | +10 stop | HYPE | DOWN | 0.69 | 0.85 | 1.36 |
| 11-16 03:41 | +20 | HYPE | DOWN | 0.69 | no | 2.95 |
| 11-16 03:41 | +15 | HYPE | DOWN | 0.62 | 0.85 | 2.04 |
| 11-16 03:41 | +10 | HYPE | DOWN | 0.62 | 0.85 | 2.04 |
| 11-16 03:41 | +5 | HYPE | DOWN | 0.62 | 0.71 | 0.58 |
| 11-16 03:32 | +10 stop | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 11-16 03:32 | +20 | NEAR | DOWN | 0.65 | 0.87 | 1.96 |
| 11-16 03:32 | +15 | NEAR | DOWN | 0.65 | 0.84 | 1.64 |
| 11-16 03:32 | +10 | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 11-16 03:32 | +5 | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 11-16 03:32 | +5 | ZEC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-16 03:32 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 11-16 03:32 | +5 | BTC | DOWN | 0.67 | 0.74 | 0.40 |
