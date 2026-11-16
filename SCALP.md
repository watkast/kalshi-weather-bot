# Range-Scalp Bot

*Updated Mon Nov 16 03:38 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61646 | 53796 | 7850 (115) | 0 | $-16556.48 | -4.3% |
| **+10¢** | 46048 | 36849 | 9199 (157) | 0 | $-15508.98 | -5.4% |
| **+15¢** | 38584 | 28662 | 9922 (196) | 0 | $-14129.18 | -5.8% |
| **+20¢** | 34394 | 23987 | 10407 (248) | 0 | $-12363.67 | -5.7% |
| **+10¢ (15¢ stop)** | 75027 | 74873 | 154 (90) | 0 | $-27624.79 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 03:32 | +10 stop | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 11-16 03:32 | +20 | NEAR | DOWN | 0.65 | 0.87 | 1.96 |
| 11-16 03:32 | +15 | NEAR | DOWN | 0.65 | 0.84 | 1.64 |
| 11-16 03:32 | +10 | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 11-16 03:32 | +5 | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 11-16 03:32 | +5 | ZEC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-16 03:32 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 11-16 03:32 | +5 | BTC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-16 03:32 | +5 | SOL | DOWN | 0.70 | 0.87 | 1.47 |
| 11-16 03:32 | +15 | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 11-16 03:32 | +10 | DOGE | DOWN | 0.71 | 0.85 | 1.16 |
| 11-16 03:32 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 11-16 03:31 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 11-16 03:31 | +20 | SOL | DOWN | 0.62 | 0.87 | 2.25 |
| 11-16 03:31 | +15 | SOL | DOWN | 0.62 | 0.87 | 2.25 |
| 11-16 03:31 | +10 | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 11-16 03:31 | +5 | SOL | DOWN | 0.62 | 0.68 | 0.27 |
| 11-16 03:31 | +10 stop | BNB | DOWN | 0.66 | 0.79 | 1.02 |
| 11-16 03:31 | +20 | BNB | DOWN | 0.67 | 0.89 | 1.97 |
| 11-16 03:31 | +15 | BNB | DOWN | 0.67 | 0.89 | 1.97 |
| 11-16 03:31 | +10 | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 11-16 03:31 | +5 | BNB | DOWN | 0.67 | 0.73 | 0.30 |
| 11-16 03:31 | +10 stop | BTC | DOWN | 0.55 | 0.68 | 0.96 |
| 11-16 03:31 | +20 | BTC | DOWN | 0.55 | 0.79 | 2.10 |
| 11-16 03:31 | +15 | BTC | DOWN | 0.55 | 0.71 | 1.27 |
| 11-16 03:31 | +10 | BTC | DOWN | 0.56 | 0.68 | 0.86 |
| 11-16 03:31 | +5 | BTC | DOWN | 0.56 | 0.61 | 0.15 |
| 11-16 03:31 | +10 stop | ZEC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-16 03:31 | +20 | ZEC | DOWN | 0.59 | 0.79 | 1.71 |
| 11-16 03:31 | +15 | ZEC | DOWN | 0.58 | 0.74 | 1.28 |
| 11-16 03:31 | +10 | ZEC | DOWN | 0.58 | 0.68 | 0.66 |
| 11-16 03:31 | +5 | ZEC | DOWN | 0.60 | 0.67 | 0.37 |
| 11-16 03:31 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-16 03:31 | +20 | ETH | DOWN | 0.59 | 0.80 | 1.81 |
| 11-16 03:31 | +15 | ETH | DOWN | 0.59 | 0.76 | 1.40 |
| 11-16 03:31 | +10 | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-16 03:31 | +5 | ETH | DOWN | 0.59 | 0.64 | 0.16 |
| 11-16 03:31 | +10 stop | HYPE | DOWN | 0.64 | 0.47 | -2.05 |
| 11-16 03:31 | +20 | HYPE | DOWN | 0.64 | 0.87 | 2.10 |
| 11-16 03:31 | +15 | HYPE | DOWN | 0.64 | 0.81 | 1.42 |
