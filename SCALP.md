# Range-Scalp Bot

*Updated Tue Nov 10 01:24 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54123 | 47215 | 6908 (89) | 4 | $-14726.82 | -4.3% |
| **+10¢** | 40428 | 32366 | 8062 (117) | 4 | $-13687.39 | -5.4% |
| **+15¢** | 33885 | 25196 | 8689 (149) | 4 | $-12449.13 | -5.9% |
| **+20¢** | 30172 | 21059 | 9113 (195) | 4 | $-10865.70 | -5.7% |
| **+10¢ (15¢ stop)** | 65931 | 65821 | 110 (66) | 3 | $-24406.26 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 01:24 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 11-10 01:24 | +10 | ZEC | DOWN | 0.70 | open |  |
| 11-10 01:24 | +5 | ZEC | DOWN | 0.70 | open |  |
| 11-10 01:23 | +5 | NEAR | DOWN | 0.70 | open |  |
| 11-10 01:22 | +10 stop | NEAR | DOWN | 0.59 | open |  |
| 11-10 01:22 | +20 | NEAR | DOWN | 0.59 | open |  |
| 11-10 01:22 | +15 | NEAR | DOWN | 0.59 | open |  |
| 11-10 01:22 | +10 | NEAR | DOWN | 0.59 | open |  |
| 11-10 01:22 | +5 | NEAR | DOWN | 0.59 | 0.64 | 0.16 |
| 11-10 01:22 | +10 stop | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-10 01:22 | +10 | ZEC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-10 01:22 | +5 | ZEC | DOWN | 0.65 | 0.72 | 0.39 |
| 11-10 01:20 | +10 stop | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 11-10 01:20 | +20 | BNB | DOWN | 0.67 | 0.88 | 1.86 |
| 11-10 01:20 | +15 | BNB | DOWN | 0.67 | 0.86 | 1.65 |
| 11-10 01:20 | +10 | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 11-10 01:20 | +5 | BNB | DOWN | 0.67 | 0.79 | 0.92 |
| 11-10 01:20 | +10 stop | HYPE | DOWN | 0.62 | 0.41 | -2.44 |
| 11-10 01:19 | +10 stop | XRP | UP | 0.65 | open |  |
| 11-10 01:18 | +5 | NEAR | DOWN | 0.65 | 0.73 | 0.46 |
| 11-10 01:18 | +10 stop | HYPE | UP | 0.59 | 0.44 | -1.85 |
| 11-10 01:18 | +10 stop | SOL | DOWN | 0.58 | 0.77 | 1.59 |
| 11-10 01:18 | +20 | SOL | DOWN | 0.58 | 0.79 | 1.76 |
| 11-10 01:18 | +15 | SOL | DOWN | 0.57 | 0.77 | 1.69 |
| 11-10 01:18 | +10 | SOL | DOWN | 0.58 | 0.77 | 1.59 |
| 11-10 01:18 | +5 | SOL | DOWN | 0.58 | 0.77 | 1.59 |
| 11-10 01:18 | +10 stop | DOGE | DOWN | 0.60 | 0.72 | 0.88 |
| 11-10 01:18 | +20 | DOGE | DOWN | 0.60 | 0.81 | 1.82 |
| 11-10 01:18 | +15 | DOGE | DOWN | 0.60 | 0.81 | 1.82 |
| 11-10 01:18 | +10 | DOGE | DOWN | 0.60 | 0.72 | 0.88 |
| 11-10 01:18 | +5 | DOGE | DOWN | 0.60 | 0.67 | 0.37 |
| 11-10 01:18 | +10 stop | NEAR | DOWN | 0.58 | 0.73 | 1.20 |
| 11-10 01:18 | +20 | NEAR | DOWN | 0.58 | 0.80 | 1.90 |
| 11-10 01:18 | +15 | NEAR | DOWN | 0.58 | 0.73 | 1.18 |
| 11-10 01:18 | +10 | NEAR | DOWN | 0.58 | 0.73 | 1.18 |
| 11-10 01:18 | +5 | NEAR | DOWN | 0.58 | 0.63 | 0.15 |
| 11-10 01:18 | +10 stop | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 11-10 01:18 | +20 | ETH | DOWN | 0.65 | 0.85 | 1.75 |
| 11-10 01:18 | +15 | ETH | DOWN | 0.65 | 0.82 | 1.43 |
| 11-10 01:18 | +10 | ETH | DOWN | 0.65 | 0.78 | 1.01 |
