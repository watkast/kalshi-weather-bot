# Range-Scalp Bot

*Updated Mon Nov 16 12:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 62106 | 54191 | 7915 (115) | 2 | $-16759.75 | -4.3% |
| **+10¢** | 46380 | 37118 | 9262 (157) | 2 | $-15623.62 | -5.4% |
| **+15¢** | 38860 | 28870 | 9990 (196) | 4 | $-14229.07 | -5.8% |
| **+20¢** | 34640 | 24167 | 10473 (249) | 6 | $-12396.28 | -5.7% |
| **+10¢ (15¢ stop)** | 75580 | 75426 | 154 (90) | 2 | $-27875.33 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 12:49 | +5 | BNB | DOWN | 0.71 | 0.81 | 0.74 |
| 11-16 12:49 | +10 stop | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-16 12:49 | +20 | BTC | DOWN | 0.65 | open |  |
| 11-16 12:49 | +15 | BTC | DOWN | 0.65 | open |  |
| 11-16 12:49 | +10 | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 11-16 12:49 | +5 | BTC | DOWN | 0.65 | 0.74 | 0.60 |
| 11-16 12:49 | +10 stop | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-16 12:49 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-16 12:49 | +5 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-16 12:48 | +15 | HYPE | DOWN | 0.67 | open |  |
| 11-16 12:48 | +5 | ETH | DOWN | 0.71 | open |  |
| 11-16 12:48 | +10 stop | HYPE | DOWN | 0.66 | open |  |
| 11-16 12:48 | +10 | HYPE | DOWN | 0.66 | open |  |
| 11-16 12:48 | +5 | HYPE | DOWN | 0.65 | open |  |
| 11-16 12:47 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 11-16 12:47 | +5 | DOGE | DOWN | 0.64 | 0.69 | 0.18 |
| 11-16 12:47 | +10 stop | HYPE | DOWN | 0.52 | 0.64 | 0.85 |
| 11-16 12:47 | +20 | HYPE | DOWN | 0.52 | open |  |
| 11-16 12:47 | +15 | HYPE | DOWN | 0.52 | 0.67 | 1.16 |
| 11-16 12:47 | +10 | HYPE | DOWN | 0.52 | 0.64 | 0.85 |
| 11-16 12:47 | +5 | HYPE | DOWN | 0.53 | 0.64 | 0.75 |
| 11-16 12:46 | +10 stop | BTC | DOWN | 0.65 | 0.83 | 1.54 |
| 11-16 12:46 | +20 | BTC | DOWN | 0.65 | 0.85 | 1.75 |
| 11-16 12:46 | +15 | BTC | DOWN | 0.65 | 0.83 | 1.54 |
| 11-16 12:46 | +10 | BTC | DOWN | 0.65 | 0.83 | 1.54 |
| 11-16 12:46 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 11-16 12:46 | +10 stop | ETH | DOWN | 0.63 | open |  |
| 11-16 12:46 | +20 | ETH | DOWN | 0.63 | open |  |
| 11-16 12:46 | +15 | ETH | DOWN | 0.63 | open |  |
| 11-16 12:46 | +10 | ETH | DOWN | 0.63 | open |  |
| 11-16 12:46 | +5 | ETH | DOWN | 0.63 | 0.69 | 0.28 |
| 11-16 12:46 | +10 stop | BNB | DOWN | 0.67 | 0.81 | 1.13 |
| 11-16 12:46 | +20 | BNB | DOWN | 0.67 | open |  |
| 11-16 12:46 | +15 | BNB | DOWN | 0.67 | open |  |
| 11-16 12:46 | +10 | BNB | DOWN | 0.67 | 0.81 | 1.15 |
| 11-16 12:46 | +5 | BNB | DOWN | 0.67 | 0.75 | 0.52 |
| 11-16 12:46 | +10 stop | SOL | DOWN | 0.65 | 0.79 | 1.12 |
| 11-16 12:46 | +20 | SOL | DOWN | 0.65 | open |  |
| 11-16 12:46 | +15 | SOL | DOWN | 0.65 | 0.81 | 1.33 |
| 11-16 12:46 | +10 | SOL | DOWN | 0.65 | 0.79 | 1.12 |
