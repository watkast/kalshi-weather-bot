# Range-Scalp Bot

*Updated Tue Nov 24 01:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70405 | 61450 | 8955 (147) | 5 | $-18850.53 | -4.3% |
| **+10¢** | 52526 | 42069 | 10457 (190) | 5 | $-17475.59 | -5.3% |
| **+15¢** | 44001 | 32738 | 11263 (246) | 8 | $-15561.90 | -5.6% |
| **+20¢** | 39180 | 27324 | 11856 (311) | 8 | $-13934.25 | -5.7% |
| **+10¢ (15¢ stop)** | 85735 | 85539 | 196 (118) | 2 | $-31545.09 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 01:34 | +10 stop | BNB | DOWN | 0.54 | 0.64 | 0.65 |
| 11-24 01:34 | +10 | BNB | DOWN | 0.54 | 0.64 | 0.65 |
| 11-24 01:34 | +5 | BNB | DOWN | 0.54 | 0.64 | 0.65 |
| 11-24 01:34 | +10 stop | ETH | DOWN | 0.55 | 0.66 | 0.76 |
| 11-24 01:34 | +10 | ETH | DOWN | 0.54 | 0.66 | 0.86 |
| 11-24 01:34 | +5 | ETH | DOWN | 0.54 | 0.66 | 0.86 |
| 11-24 01:33 | +5 | HYPE | DOWN | 0.70 | open |  |
| 11-24 01:33 | +5 | SOL | DOWN | 0.60 | open |  |
| 11-24 01:33 | +5 | XRP | DOWN | 0.58 | open |  |
| 11-24 01:32 | +10 stop | BNB | DOWN | 0.60 | 0.74 | 1.09 |
| 11-24 01:32 | +20 | BNB | DOWN | 0.60 | open |  |
| 11-24 01:32 | +15 | BNB | DOWN | 0.61 | open |  |
| 11-24 01:32 | +10 | BNB | DOWN | 0.61 | 0.74 | 0.99 |
| 11-24 01:32 | +5 | BNB | DOWN | 0.61 | 0.74 | 0.99 |
| 11-24 01:32 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-24 01:32 | +20 | ETH | DOWN | 0.65 | open |  |
| 11-24 01:32 | +15 | ETH | DOWN | 0.65 | open |  |
| 11-24 01:32 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-24 01:32 | +5 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-24 01:32 | +10 stop | HYPE | DOWN | 0.68 | 0.49 | -2.24 |
| 11-24 01:32 | +20 | HYPE | DOWN | 0.68 | open |  |
| 11-24 01:32 | +15 | HYPE | DOWN | 0.67 | open |  |
| 11-24 01:32 | +10 | HYPE | DOWN | 0.66 | open |  |
| 11-24 01:32 | +5 | HYPE | DOWN | 0.66 | 0.74 | 0.50 |
| 11-24 01:32 | +5 | SOL | DOWN | 0.58 | 0.64 | 0.25 |
| 11-24 01:31 | +10 stop | XRP | DOWN | 0.68 | 0.40 | -3.13 |
| 11-24 01:31 | +20 | XRP | DOWN | 0.66 | open |  |
| 11-24 01:31 | +15 | XRP | DOWN | 0.65 | open |  |
| 11-24 01:31 | +10 | XRP | DOWN | 0.65 | open |  |
| 11-24 01:31 | +5 | XRP | DOWN | 0.65 | 0.71 | 0.26 |
| 11-24 01:31 | +10 stop | DOGE | DOWN | 0.70 | 0.46 | -2.73 |
| 11-24 01:31 | +20 | DOGE | DOWN | 0.70 | open |  |
| 11-24 01:31 | +15 | DOGE | DOWN | 0.70 | open |  |
| 11-24 01:31 | +10 | DOGE | DOWN | 0.70 | open |  |
| 11-24 01:31 | +5 | DOGE | DOWN | 0.70 | open |  |
| 11-24 01:31 | +10 stop | SOL | DOWN | 0.67 | 0.49 | -2.14 |
| 11-24 01:31 | +20 | SOL | DOWN | 0.67 | open |  |
| 11-24 01:31 | +15 | SOL | DOWN | 0.67 | open |  |
| 11-24 01:31 | +10 | SOL | DOWN | 0.66 | open |  |
| 11-24 01:31 | +5 | SOL | DOWN | 0.66 | 0.73 | 0.37 |
